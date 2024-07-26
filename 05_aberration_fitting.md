---
title: Aberration Fitting
short_title: Aberration Fitting
label: aberration_fitting_page
---

## Aberration Surface Gradients

The cross-correlation vector shifts $\vec{w}(\vec{k})$ we computed in [](#cross_correlation_page) are given by the gradient of the aberration surface $\chi(\vec{k})$ [@lupini2016rapid]

```{math}
:label: aberration_surface_gradient_eq
\vec{w}(\vec{k}) = \nabla \chi(\vec{k}),
```

where $\vec{k}$ is the 2D Fourier space coordinate (spatial frequency) and the aberration surface can be expressed using the following expansion [@ophus2016correcting]

```{math}
:label: chi_expansion_eq
\begin{aligned}
  \chi(\vec{k}) = \frac{2\pi}{\lambda} \sum_{m,n} \frac{\left(\lambda \; |\vec{k}| \right)^{m+1}}{m+1} \Big( & C_{m,n}^x \cos{\left[n \times \mathrm{atan2}\left(k_y, k_x\right) \right]}  + \Big. \\ 
    \Big. & C_{m,n}^y \sin{\left[n \times \mathrm{atan2}\left(k_y, k_x\right) \right]}\Big),
\end{aligned}
```

$\lambda$ is the (relativistically-corrected) electron wavelength, $C_{m,n}^{x/y}$ are the Cartesian aberration coefficients of radial order $m+1$ and angular order $n$ in units of ångströms.

[](#py4dstem_parallax_shifts_interactive) investigates the effect of common aberrations and microscope geometry variations, away from the ground-truth values (relative rotation angle = -15°, and defocus = 1.5μm), on the apparent image shifts of virtual BF images and the aligned virtual BF stack.

:::{figure} #app:py4dstem_parallax_shifts_interactive
:name: py4dstem_parallax_shifts_interactive
:placeholder: ./static/py4dstem_parallax_shifts_interactive.png
**Common aberrations and microscope geometry effects on tcBF-STEM.** 
Notice the relative robustness of the aligned BF stack when the `rotation_angle` and `defocus` sliders are moved slightly away from their ground-truth values. 
Other aberrations, such as astigmatism and coma, introduce more pronnounced effects.
:::

## Aberration Fitting

Equations [](#aberration_surface_gradient_eq) and [](#chi_expansion_eq) form a linear system of equations suggesting that, given the measured vector shifts $\vec{w}(\vec{k})$, the aberration coefficients $C_{m,n}^{x/y}$, and hence $\chi(\vec{k})$, can be estimated.

Specifically, we perform the following steps:
1. estimate a 2x2 affine transformation, $H\equiv\hat{H}(\vec{k},\vec{k}')$, which maps the initial BF pixel positions, $V\equiv\vec{v}(\vec{k}')$, to the measured vector shifts, $W\equiv\vec{w}(\vec{k})$:

```{math}
:label: affine_transformation_eq
H = \left( V^T V\right)^{-1} V^T W.
```

2. decompose the affine transform into radial, $P$, and rotational, $U$, components &ndash; from which the passive rotation $\theta$ can be estimated:

```{math}
:label: polar_decomposition_eq
\begin{aligned}
  H &= U P, \\
  U &= \begin{bmatrix}
        \cos(\theta) & \sin(\theta) \\
        -\sin(\theta) & \cos(\theta) 
        \end{bmatrix}.
\end{aligned}
```

3. passively-rotate the Fourier coordinate system:
```{math}
:label: rotated_coordinate_system_eq
\vec{k}'\equiv \left(k_x,k_y\right) \to \left(k_x \cos(\theta) + k_y \sin(\theta), k_y \cos(\theta) - k_x \sin(\theta)\right).
```

4. evaluate the linear system given by Equations [](#aberration_surface_gradient_eq) and [](#chi_expansion_eq) on $\vec{k}'$ to estimate aberration coefficients $C_{m,n}^{x/y}$ up to speficied radial and angular orders {cite:p}`cowley1979coherent,lupini2010aberration,lupini2016rapid`

[](#py4dstem_parallax_fitting_bf) performs the least-squares fit for various radial and angular orders, and plots a comparison between the measured and predicted vector shifts.


:::{figure} #app:py4dstem_parallax_fitting_bf
:name: py4dstem_parallax_fitting_bf
:placeholder: ./static/py4dstem_parallax_fitting_bf.png
**Least-squares tcBF-STEM aberration fitting.** 
Notice how the fit is robust against including higher orders in the aberration expansion, despite the ground-truth shifts including only defocus.
:::

