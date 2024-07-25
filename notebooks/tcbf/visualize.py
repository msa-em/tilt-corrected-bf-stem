import numpy as np
from matplotlib import cm, colors as mcolors, pyplot as plt
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from mpl_toolkits.axes_grid1 import make_axes_locatable
from colorspacious import cspace_convert

def return_scaled_histogram(
    array,
    vmin=None,
    vmax=None,
):
    if np.isclose(np.max(array), np.min(array)):
        if vmin is None:
            vmin = 0
        if vmax is None:
            vmax = np.max(array)
    else:
        if vmin is None:
            vmin = 0.02
        if vmax is None:
            vmax = 0.98

        vals = np.sort(array[~np.isnan(array)])
        ind_vmin = np.round((vals.shape[0] - 1) * vmin).astype("int")
        ind_vmax = np.round((vals.shape[0] - 1) * vmax).astype("int")
        ind_vmin = np.max([0, ind_vmin])
        ind_vmax = np.min([len(vals) - 1, ind_vmax])
        vmin = vals[ind_vmin]
        vmax = vals[ind_vmax]

    array = np.where(array < vmin, vmin, array)
    array = np.where(array > vmax, vmax, array)

    return array, vmin, vmax


def Complex2RGB(
    complex_data, vmin=None, vmax=None, power=None, chroma_boost=1
):
    """ """
    amp = np.abs(complex_data)
    phase = np.angle(complex_data)

    if power is not None:
        amp = amp**power

    amp, vmin, vmax = return_scaled_histogram(amp, vmin, vmax)
    amp = ((amp - vmin) / vmax).clip(1e-16, 1)

    J = amp * 61.5  # Note we restrict luminance to the monotonic chroma cutoff
    C = np.minimum(chroma_boost * 98 * J / 123, 110)
    h = np.rad2deg(phase) + 180

    JCh = np.stack((J, C, h), axis=-1)
    rgb = cspace_convert(JCh, "JCh", "sRGB1").clip(0, 1)

    return rgb


def add_scalebar(ax, length, sampling, units, color="white", size_vertical=1, pad=0.5):
    """ """
    bar = AnchoredSizeBar(
        ax.transData,
        length,
        f"{sampling*length:.2f} {units}",
        "lower right",
        pad=pad,
        color=color,
        frameon=False,
        label_top=True,
        size_vertical=size_vertical,
    )
    ax.add_artist(bar)
    return ax, bar


def add_colorbar_arg(cax, chroma_boost=1, c=49, j=61.5):
    """
    cax                 : axis to add cbar to
    chroma_boost (float): boosts chroma for higher-contrast (~1-2.25)
    c (float)           : constant chroma value
    j (float)           : constant luminance value
    """

    h = np.linspace(0, 360, 256, endpoint=False)
    J = np.full_like(h, j)
    C = np.full_like(h, np.minimum(c * chroma_boost, 110))
    JCh = np.stack((J, C, h), axis=-1)
    rgb_vals = cspace_convert(JCh, "JCh", "sRGB1").clip(0, 1)
    newcmp = mcolors.ListedColormap(rgb_vals)
    norm = mcolors.Normalize(vmin=-np.pi, vmax=np.pi)

    cb = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=newcmp), cax=cax)

    cb.set_label("arg", rotation=0, ha="center", va="bottom")
    cb.ax.yaxis.set_label_coords(0.5, 1.01)
    cb.set_ticks(np.array([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]))
    cb.set_ticklabels(
        [r"$-\pi$", r"$-\dfrac{\pi}{2}$", "$0$", r"$\dfrac{\pi}{2}$", r"$\pi$"]
    )


def show_complex(
    complex_data,
    figax=None,
    vmin=None,
    vmax=None,
    power=None,
    ticks=True,
    chroma_boost=1,
    cbar=True,
    **kwargs,
):
    """ """
    rgb = Complex2RGB(
        complex_data, vmin, vmax, power=power, chroma_boost=chroma_boost
    )

    figsize = kwargs.pop("figsize", (6, 6))
    if figax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig, ax = figax

    ax.imshow(rgb, interpolation=None, **kwargs)

    if cbar:
        divider = make_axes_locatable(ax)
        ax_cb = divider.append_axes("right", size="5%", pad="2.5%")
        add_colorbar_arg(ax_cb, chroma_boost=chroma_boost)

    if ticks is False:
        ax.set_xticks([])
        ax.set_yticks([])

    return ax


def show(
    array,
    figax=None,
    vmin=None,
    vmax=None,
    power=None,
    ticks=True,
    cbar=True,
    cmap="gray",
    **kwargs,
):
    """ """

    if power is not None:
        array = array**power

    array, vmin, vmax = return_scaled_histogram(array, vmin, vmax)
    # array = (array - vmin) / vmax

    figsize = kwargs.pop("figsize", (6, 6))
    if figax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig, ax = figax

    ax.imshow(
        array, vmin=vmin, vmax=vmax, cmap=cmap, interpolation='bicubic', **kwargs
    )

    if cbar:
        divider = make_axes_locatable(ax)
        ax_cb = divider.append_axes("right", size="5%", pad="2.5%")

        norm = mcolors.Normalize(vmin=0, vmax=1)
        cb = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=ax_cb)

    if ticks is False:
        ax.set_xticks([])
        ax.set_yticks([])

    return ax