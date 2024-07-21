---
title: Phase Problem in Electron Microscopy
short_title: EM Phase Problem
---

:::{caution} TO-DO:
- Add text describing phase problem in electron microscopy
- Add Zernike phase-plate equation
:::

(intro)= 
# Introduction

One of the most powerful operating modes for transmission electron microscopy (TEM) is *phase contrast imaging* where imaging optics or detector configurations are used to convert phase modulations of the electron beam into intensity variations {cite:p}`carter2016transmission`. The simplest method to produce phase contrast in plane wave TEM imaging is to apply under- or over-focus to the electron wave after it interacts with the sample, shown in [](#phase_problem_em). The sample shown here is (a protein), which produces very weak diffraction of the electron beam. To produce usable contrast, we must either apply a large defocus or increase the electron fluence, often colloquially referred to as the electron dose {cite:p}`egerton2021dose`. 


```{figure} #app:phase_problem_em
:name: phase_problem_em
:placeholder: ./static/phase_problem_em.png
**Plane wave HRTEM imaging simulation of (a protein).** When the defocus is zero, this weakly-scattering sample produces only a small amount of amplitude constast. By defocusing the scattered electron wave or introducing a Zernike phase plate, we can increase the contrast. This produces measurable intensity variations even for very low electron fluence.
```






<!-- :::{figure} #app:phase_problem_em
:name: phase_problem_em
:placeholder: ./static/phase_problem_em.png
Phase problem in electron microscopy. 
::: -->




