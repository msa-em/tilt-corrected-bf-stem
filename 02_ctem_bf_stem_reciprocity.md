---
title: Conventional TEM / Bright-Field STEM Reciprocity
short_title: CTEM / BF-STEM Reciprocity
label: reciprocity_page
---

### Conventional TEM

Conventional transmission electron microscopy (CTEM) refers to a TEM imaging mode where we form a plane-wave of electrons focused on (or close to) an electron-transparent sample [@de2003introduction].
In bright field (BF) CTEM imaging we use a post-specimen aperture which only allows unscattered electrons to hit the detector. 
Alternatively we can produce a dark field (DF) image by using an aperture to select a subset of the scattered electrons. 
As discussed in [](#phase_contrast_imaging_page), we can use a phase plate or defocus to produce contrast without an aperture.
CTEM is widely used for imaging biological specimens [@cheng2015single], weakly-scattering materials science or geological samples [@lee2010transmission], and for *in situ* experiments where we typically want high temporal resolution while observing a large field of view [@ross2007situ].

### Scanning TEM

An alternative imaging mode to CTEM is [scanning transmission electron microscopy](wiki:Scanning_transmission_electron_microscopy) (STEM) [@pennycook2011scanning].
In STEM, we use a large aperture in the condenser plane, which forms an electron probe composed of a cone of illumination angles. 
The objective lens focuses this probe onto the sample, and electromagnetic or electrostatic *scan coils* are used to raster the probe over the sample surface [@grigson1965improved]. 
STEM has many flexible imaging and diffraction modes as well as the ability to collect spectroscopic signals such such as x-ray energy dispersive spectrometry (XEDS) [@watanabe2016practical] and electron energy loss spectroscopy (EELS) [@egerton2008electron], and is therefore widely used in materials science studies [@ophus2023quantitative]. 
In BF STEM, we measure the diffracted electron beam in the far field, using a detector centered on the optical axis which covers either a subset of the illumination angles or the full illumination cone [@lebeau2009quantitative].

:::{figure} #app:ctem_bf_stem_reciprocity
:name: ctem_bf_stem_reciprocity
:placeholder: ./static/ctem_bf_stem_reciprocity.png
Principle of reciprocity in off-axis BF-STEM and tilted CTEM.
The deflected ray traces in CTEM from source-to-detector match the ray traces in STEM from detector-to-source, and highlight the apparent image shifts at the sample plane.
:::

### Principle of Reciprocity


CTEM and BF STEM can be related using the concept of [reciprocity](wiki:Helmholtz_reciprocity). 
The principle of reciprocity in electron microscopy states that rays connecting a source to a detector follow the same optical path as the rays from the detector to the source [@krause2017reciprocity]. 
[](#ctem_bf_stem_reciprocity) shows how this principle applies to CTEM and BF STEM, if we swap the source and detector positions for the STEM diagram. 

By following the deflected rays from source-to-detector in CTEM and detector-to-source in STEM we can see reciprocity in action.
Notice also how the deflected rays impact the sample at different positions, giving rise to the apparent image shifts the tcBF-STEM technique uses to reconstruct the phase, and how the magnitude of these shifts depend of the defocus as we will investigate in [](#virtual_bf_page).
