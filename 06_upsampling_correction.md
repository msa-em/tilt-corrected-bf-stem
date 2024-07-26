---
title: Upsampling of Aligned Bright Field
short_title: Upsampling of Aligned BF
label: upsampling_page
---

### Subpixel Upsampling

As alluded to in previous sections, one of the strengths of tcBF-STEM is the fact that its resolution is not limited by the scan sampling, but rather controlled by the subpixel accuracy of the measured cross-correlation vector shifts, and ultimately limited by twice the convergence semi-angle [@varnavides2023iterative].
In order to extract this additional resolution, we need to upsample our aligned virtual BF images stack using the following py4DSTEM snippet:

```python
parallax = parallax.subpixel_alignment(
    kde_upsample_factor=4,
    plot_upsampled_BF_comparison=False,
    plot_upsampled_FFT_comparison=False,
)
```

:::{figure} #app:py4dstem_parallax_subpixel
:name: py4dstem_parallax_subpixel
:placeholder: ./static/py4dstem_parallax_subpixel.png
**Subpixel upsampling using kernel density estimation.**
:::

Note this does not simply perform Fourier upsampling, as can be seen from the additional Thon ring-like oscillations beyond the Nyquist scan-sampling limit.
Instead, the sub-pixel accurate cross-correlation vector shifts are used to interpolating the virtual BF images stack using [kernel density estimation](wiki:Kernel_density_estimation) (KDE) interpolation [@ophus2016correcting].
Play around with the slider above to get a sense of how much additional resolution can be gained using KDE interpolation.

### Aberration Correction

Notice how the aligned and upsampled virtual BF images we have investigated so far all have BF CTEM-like contrast.
To account for this, and obtain contrast similar to that of the projected potential, we can use the estimated aberration coefficients to perform contrast transfer function (CTF) correction.

This correction can take many forms, but in py4DSTEM we choose to simply flip the sign of the even aberration coefficients and correct the asymmetry introduced by odd aberration coefficients using the following Fourier-space filter {cite:p}`lupini2016rapid,varnavides2023iterative`

```{math}
:label: aberration_correction_eq
\xi(\boldsymbol{k}) =  \mathrm{sign} \left[ \sin\left(\chi^{\mathrm{even}}(\boldsymbol{k})\right) \right] \times \exp \left[-\mathrm{i} \chi^{\mathrm{odd}}(\boldsymbol{k}) \right]
```

:::{figure} #app:py4dstem_parallax_correction
:name: py4dstem_parallax_correction
**Aberration correction of the KDE upsampled image.**
:::

[](#py4dstem_parallax_correction) plots the aberration-corrected image following upsampling, which can be achieved using the following py4DSTEM snipppet:

```python
parallax = parallax.aberration_correct(
    use_CTF_fit=True,
    figsize=(6,3),
    cmap='gray',
)
```

