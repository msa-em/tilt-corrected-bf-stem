---
title: Cross-Correlation of Virtual Bright-Field Images
short_title: Cross-Correlation
label: cross_correlation_page
---

### Tilt-Corrected Virtual BFs

The simulations shown in [](#virtual_bf_page) used very fine sampling in both real-space (STEM probe positions) and Fourier-space (4D-STEM detector pixels).
As we will see in [](#upsampling_page) one of the advantages of tcBF-STEM is that it drastically reduces both these sampling requirements, allowing us to collect more dose-efficient datasets.
In the remaining pages, we will work with a simulated 4D-STEM dataset using the same apoferritin sample, with the more realistic dimensions of $\left(R_x,R_y,Q_x,Q_y\right)=(24,48,128,128)$, i.e. $128 \times 128$ pixel diffraction patterns collected on a grid of $24 \times 48$ probe positions, with a spacing of $\sim 1$ nm and an electron dose of $100 \; e/\AA^2$.

[](#py4dstem_parallax_vbfs) illustrates the BF disk on the left, and the virtual BF images formed by the center-most pixel (right, magenta).
Notice how much more noisy the virtual BF images look at realistic sampling conditions, as compared to [](#virtual_bf_images_stack).
We can bin the diffraction pattern further, to increase the signal-to-noise ratio (SNR) of the virtual BF images, by summing the intensity of nearby pixels together.

Play around with the slider below to increase the radius of the magenta pixels summed to produce the virtual BF image; you should find that while initially the SNR increases slightly, the faint protein signal gets blurred as we approach the radius of the BF disk to form what is referred to as an incoherent BF image (right, cyan).
This is because, as we saw in [](#virtual_bf_page), the further away we get from the optical axis the greater the magnitude of the apparent shift of each virtual BF image and thus when averaged together introduces blurring.
This is precisely the operation tcBF-STEM aims to "undo".

:::{figure} #app:py4dstem_parallax_vbfs
:name: py4dstem_parallax_vbfs
:placeholder: ./static/py4dstem_parallax_vbfs.png
Virtual BF images formed by summing axial pixels (right, magenta) of a specific radius and the entire BF disk to form an incoherent BF image (right, cyan), for a simulated dataset of an apoferritin protein using typical sampling parameters and an electron dose of $100 \; e/\AA^2$.
:::

### Iterative Alignment Bins

Put simply what the tcBF-STEM algorithm attempts to do is to estimate the apparent image shifts of off-axis virtual BF images; align them with the optical axis; and sum their shifted intensity to boost the SNR and bring all the virtual BF images in registry.
In the open-source tcBF-STEM implementation in [py4DSTEM](https://github.com/py4dstem/py4DSTEM) [@varnavides2023iterative] this is achieved by employing a similarity measure called [cross-correlation](wiki:Cross-correlation).

To ensure this procedure is robust against low SNR virtual BF images we implement an iterative cross-correlation scheme, where we estimate the cross-correlation vector field by binning the BF disk in decreasing smaller bin values and using the previous cross-correlation values as a starting guess for subsequent iterations.
[](#py4dstem_parallax_masks) plots the the virtual BF masks used to compute the cross-correlation vector fields at each iteration.

:::{figure} #app:py4dstem_parallax_masks
:name: py4dstem_parallax_masks
Virtual BF masks used to compute the tcBF-STEM cross-correlation shifts at decreasing bin values.
:::

### Iterative Cross-Correlation

:::{caution} TO-DO:
- Add text describing iterative cross-correlation
:::

:::{figure} #app:py4dstem_parallax_reconstruct
:name: py4dstem_parallax_reconstruct
py4DSTEM parallax iterative cross-correlation
:::

### Cross-Correlation Shifts

:::{caution} TO-DO:
- Add text describing cross-correlation shifts surface
:::

:::{figure} #app:py4dstem_parallax_shifts
:name: py4dstem_parallax_shifts
:placeholder: ./static/py4dstem_parallax_shifts.png
py4DSTEM parallax iterative cross-correlation
:::

