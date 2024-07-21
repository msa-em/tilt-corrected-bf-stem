---
title: Virtual Bright-Field Images Stack
short_title: Virtual BF Images Stack
label: virtual_bf_page
---

<!-- :::{caution} TO-DO:
- Add text describing visual demo of principle of reciprocity
  - Explain how 4D-data gets transformed to virtual BFs stack
::: -->

Using the principles of reciprocity described in [](#reciprocity_page), we can examine in more detail how aberrations impact virtual imaging in STEM. First, we can consider the image resulting from the center most pixel of a bright field disk. This image is formed by integrating in reciprocal space the area highlighted by the red dot to produce a 2D-real space image from a 4D-STEM data. This image is analogous to a conventional TEM image at the same conditions. More generally in STEM imaging, as the collection angle is decreased, diffraction contrast increases, and the resulting image looks more like a TEM bright field image {cite:p}`carter2016transmission`. Using the defocus slider in [](#virtual_bf_images_stack), you can see the contrast changes and Fresnel ringing the arises in conventional TEM imaging as a function of aberrations. 

However, the STEM probe is made of many pixels, each of which is anologous to an incoming plane wave for TEM imaging but at a different tilt. When defocused, the tilted illumination produces image shifts, which can be seen by changing the kx and ky sliders in [](#virtual_bf_images_stack). The impact of various aberrations on the shifts is explored in more detail in [](#phase_problem_em_page).

:::{figure} #app:virtual_bf_images_stack
:name: virtual_bf_images_stack
:placeholder: ./static/virtual_bf_images_stack.png
**Virtual Bright-Field Images.** The virtual images (right) are formed from the location shown from the red dot (left). The size of the shift and fringes in the image become larger with increasing magnitude of defocus.
:::

The first step in tilt-corrected bright field imaging is to identify the pixels that make up the bright field disk in a 4D-STEM dataset. Each pixel in diffraciton space can be integrated to form a virtual image. Therefore, the 4D-STEM array (Rx, Ry, Qx, Qy) can be integrated to form an image stack (N, Qx, Qy), where N is the number of pixels in the bright field disk. 

