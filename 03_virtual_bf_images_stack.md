---
title: Virtual Bright-Field Images Stack
short_title: Virtual BF Images Stack
label: virtual_bf_page
---

The STEM discussion in [](#reciprocity_page) describe a conventional BF detector, which records a single intensity value per STEM probe position. 
However, with high-speed direct electron detectors, we can record a full image of the diffracted electron beam at each probe position [@tate2016high]. 
By recording 2D images of of the STEM probe over a 2D grid of probe positions, we produce a four dimensonal dataset. 
This family of STEM methods is often referred to as four dimensional STEM (4D-STEM) [@ophus2019four]. 
We can produce BF STEM images from a 4D-STEM dataset by using virtual detectors composed of integration masks applied in the diffraction space dimensions of a 4D-STEM dataset [@ribet2023defect].
 The algorithmic and software implementation for various phase contrast 4D-STEM imaging methods are described in the manuscript by {cite:t}`varnavides2023iterative`.

Using the principles of reciprocity described in [](#reciprocity_page), we can examine in more detail how aberrations impact virtual imaging in STEM. 
First, we can consider the image resulting from the center most pixel of a bright field disk. 
This image is formed by integrating in reciprocal space the area highlighted by the red dot in [](#virtual_bf_images_stack) to produce a 2D-real space image from a 4D-STEM data. 
This image is analogous to a conventional TEM image at the same conditions. 
More generally in STEM imaging, as the collection angle is decreased, diffraction contrast increases, and the resulting image looks more like a TEM bright field image [@carter2016transmission]. 
Using the defocus slider in [](#virtual_bf_images_stack), you can see in the image on the right the contrast changes and Fresnel ringing that arises in conventional TEM imaging as a function of aberrations. 


:::{figure} #app:virtual_bf_images_stack
:name: virtual_bf_images_stack
:placeholder: ./static/virtual_bf_images_stack.png
**Virtual Bright-Field Images.** Schematic of STEM probe (left). 
The virtual images (right) are formed from the position highlighted by the red dot (middle). 
The size of the shift and fringes in the image become larger with increasing magnitude of defocus.
:::


As we saw, the STEM probe covers many pixels in diffraction space, each of which is analogous to an incoming plane wave for TEM imaging but at a different tilt. 
When defocused, the tilted illumination produces image shifts, which can be seen by changing the $k_x$ and $k_y$ sliders in [](#virtual_bf_images_stack). 
The magnitude of the shifts changes with increasing defocus, which is based on the geometry of a defocused probe, as illustrated on the left.
The impact of various aberrations on the shifts is explored in more detail in [](#aberration_fitting_page).


