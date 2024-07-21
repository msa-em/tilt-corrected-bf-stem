---
title: Aberration Fitting
short_title: Aberration Fitting
label: aberration_fitting_page
---

## Aberration Surface Gradients

The cross-correlation vector shifts $\boldsymbol{w}(\boldsymbol{k})$ we computed in [](#cross_correlation_page) are proportional to the gradient of the aberration surface $\chi(\boldsymbol{k})$ {cite:p}`lupini2016rapid`:

```{math}
:label: aberration_surface_gradient_eq
\boldsymbol{w}(\boldsymbol{k}) \propto \nabla \chi(\boldsymbol{k}),
```

where $\boldsymbol{k}$ is the 2D reciprocal-space coordinate (spatial frequency) and the aberration surface can be expressed using the following expansion {cite:p}`ophus2016correcting`:

```{math}
:label: chi_expansion_eq
\chi(\boldsymbol{k}) = \frac{2\pi}{\lambda} \sum_{m,n} \frac{\left(\lambda \; k \right)^{m+1}}{m+1} \Big( & C_{m,n}^x \cos{\left[n \times \mathrm{atan2}\left(k_y, k_x\right) \right]}  + \Big. \notag \\ 
    \Big. & C_{m,n}^y \sin{\left[n \times \mathrm{atan2}\left(k_y, k_x\right) \right]}\Big),
```

where $\lambda$ is the electron wavelength, $C_{m,n}^{x/y}$ are the Cartesian aberration coefficients of radial order $m+1$ and angular order $n$ in units of ångströms.

[](#py4dstem_parallax_shifts_interactive) below investigates the effect of common aberrations and microscope geometry variations, away from the ground-truth simulated values (relative rotation angle = -15°, and defocus = 1.5μm), on the apparent image shifts of virtual BF images and the aligned virtual BF stack.

:::{figure} #app:py4dstem_parallax_shifts_interactive
:name: py4dstem_parallax_shifts_interactive
:placeholder: ./static/py4dstem_parallax_shifts_interactive.png
**Common aberrations and microscope geometry effects on tcBF-STEM.** Notice the relative robustness of the aligned BF stack when the `rotation_angle` and `defocus` sliders are moved slightly away from their ground-truth simulated values. Other aberrations, such as astigmatism and coma, introduce more pronnounced effects.
:::

### Aberration Fitting - Higher Order

:::{caution} TO-DO:
- Add text and equations describing least-squares fitting
:::

:::{figure} #app:py4dstem_parallax_fitting_bf
:name: py4dstem_parallax_fitting_bf
:placeholder: ./static/py4dstem_parallax_fitting_bf.png
py4DSTEM parallax aberration fitting
:::

