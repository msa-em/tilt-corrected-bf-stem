---
title: Phase Contrast Imaging
label: phase_contrast_imaging_page
---

### Introduction

One of the most powerful operating modes for [transmission electron microscopy](wiki:Transmission_electron_microscopy) (TEM) is [phase contrast imaging](wiki:Phase-contrast_imaging) (PCI) where imaging optics or detector configurations are used to convert phase modulations of the electron beam into intensity variations {cite:p}`carter2016transmission`.
The simplest method to produce phase contrast in plane wave TEM imaging is to apply under- or over-focus to the electron wave after it interacts with the sample, shown in [](#phase_contrast_imaging).
The protein sample shown here is [apoferritin](https://www.rcsb.org/structure/8RQB), which produces very weak diffraction of the electron beam.
To produce usable contrast from defocus, we must either apply a large defocus or increase the electron fluence, colloquially referred to as the electron dose [@egerton2021dose]. 


```{figure} #app:phase_contrast_imaging
:label: phase_contrast_imaging
:placeholder: ./static/phase_contrast_imaging.png
**{abbr}`Plane wave HRTEM imaging simulation of apoferritin (Press the button on the upper right to get an interactive figure - try changing the defocus, electron dose, or zooming in!)`.**
When the defocus is zero, this weakly-scattering sample produces only a small amount of amplitude contrast.
By defocusing the scattered electron wave or introducing a Zernike phase plate (plotted with the sign convention as the sample potential), we can increase the contrast.
This produces measurable intensity variations even for very low electron fluence.
```

Conventional TEM experiments cannot directly measure phase.
Our detectors measure only the intensity (squared amplitude) $I(\vec{r})$  of the electron [wavefunction](wiki:Wave_function) $\Psi(\vec{r})$
```{math}
:label: eq:intensity_detector

\begin{align} 
	I(\vec{r}) = |\Psi(\vec{r})|^2
\end{align}.
```

### Imaging with Defocus


Defocusing an electron wavefunction $\psi_0(\vec{r})$ by a distance $\Delta f$ to produce the output wave $\psi(\vec{r})$ can be modeled mathematically using the expression
```{math}
:label: eq:defocus_real

\psi(\vec{r}) = \psi_0(\vec{r})
	\circledast \frac{i}{\lambda \Delta f}
	\exp \left( \frac{i |\vec{r}|^2}{2 \lambda \Delta f} \right)
```
where $\lambda$ is the (relativistically-corrected) electron wavelength, $i$ is the imaginary constant, and $\circledast$ is the 2D convolution operator.
This expression is not practical for numerical calculations, and so we use the [convolution theorem](wiki:Convolution_theorem) to defocus the wave using 2D [fast Fourier transforms](wiki:Fast_Fourier_transform) (FFT), given by the expression 
```{math}
:label: eq:defocus_fft
\Psi(\vec{k}) = \Psi_0(\vec{k})
	\exp \left( -i \pi \lambda \Delta f \right)
```
where $\Psi(\vec{k})= \mathscr{F}_{r \rightarrow k}\{\psi(\vec{r})\}$ is the 2D [Fast Fourier transform](wiki:Fast_Fourier_transform) between the real space coordinates $\vec{r}$ and Fourier space coordinates $\vec{k}$.
The electron wavefunction after interacting with a weakly-scattering sample can be approximated as
```{math}
:label: eq:weak_phase_object
\psi_0(\vec{r}) = 
	1 + i \phi(\vec{r}),
```
where the $\phi(\vec{r})$ is the phase shift imparted by the sample, and it is considered to be a weak phase object [@vulovic2014use]. Combining equations [](#eq:defocus_fft)
 and [](#eq:weak_phase_object), we can derive the measured intensity for a weak phase object to be
```{math}
:label: eq:intensity_wpo_defocus
I(\vec{r}) = 
	1 - 2 \phi(\vec{r}) 
	\circledast 
	\mathscr{F}_{k \rightarrow r}\{  
		\sin \left( \pi \lambda \Delta f \right)
	\}
```

### Imaging with a Phase Plate

An alternative PCI method for plane wave TEM is to use a post-specimen phase plate which advances the phase of the unscattered zero beam with respect to the scattered electrons, or vice versa.
These phase plates have various designs, including a Zernike phase plate {cite:p}`zernike1942phase`, Boersch phase plate {cite:p}`boersch1947kontraste`, Volta phase plate {cite:p}`danev2014volta`, or the recently developed laser phase plates {cite:p}`schwartz2017near`.
An ideal phase plate can be modeled in diffraction space using the expression
```{math}
:label: eq:phase_plate
\Psi(\vec{k}) = \Psi_0(\vec{k}) (1 - \delta(\vec{k})) + i \delta(\vec{k})
```
where $\delta(\vec{k})$ is the [Delta Dirac function](wiki:Dirac_delta_function).
[](#phase_contrast_imaging) shows how (idealized) phase plate PCI compares to defocusing the sample. The sample intensity for a weak phase object is given by the expression
```{math}
:label: eq:intensity_wpo_phase_plate
I(\vec{r}) = 
	1 + 2 \phi(\vec{r}) 
```

We note however that practical implementations of phase plates remaining challenging, and typically do not perform as well as the ideal case shown above [@nagayama2011another].

