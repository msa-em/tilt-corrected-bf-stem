---
title: Cross-Correlation of Virtual Bright-Field Images
short_title: Cross-Correlation
label: cross_correlation_page
---

### Tilt-Corrected Virtual BFs

The simulations shown in [](#virtual_bf_page) used very fine sampling in both real-space (STEM probe positions) and Fourier-space (4D-STEM detector pixels).
As we will see in [](#upsampling_page), one of the advantages of tcBF-STEM is that it drastically reduces both these sampling requirements, allowing us to collect more dose-efficient datasets [@yu2024dose].
In the remaining pages, we will work with a simulated 4D-STEM dataset using the same apoferritin sample, with the more realistic dimensions of $\left(R_x,R_y,Q_x,Q_y\right)=(24,48,128,128)$, i.e. $128 \times 128$ pixel diffraction patterns collected on a grid of $24 \times 48$ probe positions, with a spacing of $\sim 1$ nm and an electron dose of $100 \; e/\rm{\AA}^2$.

[](#py4dstem_parallax_vbfs) illustrates the BF disk on the left and a virtual BF image formed by the center-most pixel (right, magenta).
Notice how much more noisy the virtual BF images look at realistic sampling conditions, as compared to [](#virtual_bf_images_stack).
We can bin the diffraction pattern further, to increase the signal-to-noise ratio (SNR) of the virtual BF images, by summing the intensity of nearby pixels together.

:::{figure} #app:py4dstem_parallax_vbfs
:name: py4dstem_parallax_vbfs
:placeholder: ./static/py4dstem_parallax_vbfs.png
**Virtual BF images** formed by summing axial pixels (right, magenta) of a specific radius and the entire BF disk to form an incoherent BF image (right, cyan), for a simulated dataset of an apoferritin protein using typical sampling parameters and an electron dose of $100 \; e/\rm{\AA}^2$.
:::

Play around with the slider below to increase the radius of the magenta pixels summed to produce the virtual BF image; you should find that while initially the SNR increases slightly, the faint protein signal gets blurred as we approach the radius of the BF disk to form what is referred to as an incoherent BF image (right, cyan).
This is because, as we saw in [](#virtual_bf_page), the further away we get from the optical axis the greater the magnitude of the apparent shift of each virtual BF image and thus when averaged together introduces blurring.
This is precisely the operation tcBF-STEM aims to "undo" [@yu2024dose].


### Iterative Alignment Bins

Put simply, what the tcBF-STEM algorithm attempts to do is to estimate the apparent image shifts of off-axis virtual BF images, align them with the optical axis, and sum their shifted intensity to boost the SNR, to bring all the virtual BF images in registry.
In the [open-source tcBF-STEM implementation](https://github.com/py4dstem/py4DSTEM) in `py4DSTEM` [@varnavides2023iterative] this is achieved by employing a similarity measure called [cross-correlation](wiki:Cross-correlation).

To ensure this procedure is robust against low SNR virtual BF images, we implement an iterative cross-correlation scheme. 
We estimate the cross-correlation vector field by binning the BF disk in decreasing smaller bin values and using the previous cross-correlation values as a starting guess for subsequent iterations.
[](#py4dstem_parallax_masks) plots the the virtual BF masks used to compute the cross-correlation vector fields at each iteration.

:::{figure} #app:py4dstem_parallax_masks
:name: py4dstem_parallax_masks
**Virtual BF masks** used to compute tcBF-STEM cross-correlation shifts at decreasing bin values.
:::

### Iterative Cross-Correlation

Despite the fact that the virtual BF images shown in [](#py4dstem_parallax_vbfs) have no discernible features the human eye can align to, iterative cross-correlation works remarkably well for this dataset.
Note that in practice one often adds fiducial markers, such as gold nanoparticles, which produce strong amplitude contrast to ensure cross-correlation succeeds for very low SNR datasets [@yu2024dose].
[](#py4dstem_parallax_reconstruct) illustrates the iterative alignment visually using the following snippet:

```python
parallax = py4DSTEM.process.phase.Parallax(
    datacube=dataset, # py4DSTEM.DataCube
    energy = 300e3, # in eV
    object_padding_px=(8,8), # in pixels
).preprocess(
    edge_blend=4, # in pixels
    plot_average_bf=False,
).reconstruct(
    alignment_bin_values=[32,32,16,16,8,8],
    progress_bar=False,
    figsize=(10,4.5),
    cmap='gray',
)
```

:::{figure} #app:py4dstem_parallax_reconstruct
:name: py4dstem_parallax_reconstruct
**Iterative cross-correlation alignment of virtual BF images in `py4DSTEM`.**
:::

Notice how much crisper the aligned virtual BF image looks like as the iterative alignment proceeds, as-well as the monotonic decrease in the self-consistent error metric.


### Cross-Correlation Shifts

In addition to the aligned BF image, it is useful to inspect the cross-correlation vector field, i.e. the 2D cross-correlation vectors as a function of BF disk pixel position, directly.
As we will see in [](#aberration_fitting_page), these hold a wealth of information pertaining to the microscope geometry and imaging conditions.
Try playing around with the slider in [](#py4dstem_parallax_shifts) to get a sense of the cross-correlation vector field.

:::{figure} #app:py4dstem_parallax_shifts
:name: py4dstem_parallax_shifts
:placeholder: ./static/py4dstem_parallax_shifts.png
**Iterative cross-correlation vector field.**
:::

