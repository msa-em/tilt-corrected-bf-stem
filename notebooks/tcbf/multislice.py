import numpy as np

# Classes


class PotentialArray:
    def __init__(self, array, slice_thickness, sampling):
        self.array = array
        self.slice_thickness = slice_thickness
        self.sampling = sampling
        self.gpts = array.shape[1:]


class CTF:
    def __init__(
        self,
        semiangle_cutoff,
        rolloff,
    ):
        self.semiangle_cutoff = semiangle_cutoff
        self.rolloff = rolloff

    def evaluate_aperture(self, alpha, phi):
        semiangle_cutoff = self.semiangle_cutoff / 1000
        if self.rolloff > 0:
            rolloff = self.rolloff / 1000
            array = 0.5 * (
                1
                + np.cos(
                    np.pi * (alpha - semiangle_cutoff + rolloff) / rolloff
                )
            )
            array[alpha > semiangle_cutoff] = 0.0
            array = np.where(
                alpha > semiangle_cutoff - rolloff,
                array,
                np.ones_like(alpha),
            )
        else:
            array = np.array(alpha < semiangle_cutoff)
        return array


class FresnelPropagator:
    def __init__(self):
        return None

    def evaluate_propagator_array(self, gpts, sampling, wavelength, dz, tilt):
        kx = np.fft.fftfreq(gpts[0], sampling[0])
        ky = np.fft.fftfreq(gpts[1], sampling[1])
        k = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2)
        f = np.exp(
            -1j * (kx[:, None] ** 2 * np.pi * wavelength * dz)
        ) * np.exp(-1j * (ky[None, :] ** 2 * np.pi * wavelength * dz))

        if tilt is not None:
            f *= np.exp(
                -1j * (kx[:, None] * np.tan(tilt[0] / 1e3) * dz * 2 * np.pi)
            )
            f *= np.exp(
                -1j * (ky[None, :] * np.tan(tilt[1] / 1e3) * dz * 2 * np.pi)
            )

        kcut = 1 / np.max(sampling) / 2 * 2 / 3
        mask = 0.5 * (1 + np.cos(np.pi * (k - kcut + 0.1) / 0.1))
        mask[k > kcut] = 0.0
        mask = np.where(k > kcut - 0.1, mask, np.ones_like(k))

        return f * mask

    def propagate(
        self,
        array,
        propagator_array,
    ):
        array_fft = np.fft.fft2(array)
        return np.fft.ifft2(array_fft * propagator_array)


class Waves:
    def __init__(self, array, sampling, wavelength, sigma, tilt):
        self.array = array
        self.sampling = sampling
        self.wavelength = wavelength
        self.sigma = sigma
        self.tilt = tilt
        self.gpts = array.shape
        self.propagator = FresnelPropagator()

    def get_spatial_frequencies(self):
        sx, sy = self.sampling
        nx, ny = self.gpts
        kx = np.fft.fftfreq(nx, sx)
        ky = np.fft.fftfreq(ny, sy)
        return kx, ky

    def get_scattering_angles(self):
        kx, ky = self.get_spatial_frequencies()
        alpha = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2) * self.wavelength
        phi = np.arctan2(ky[None, :], kx[:, None])
        return alpha, phi

    def multislice(self, potential):
        dz = potential.slice_thickness
        out_array = self.array.copy()
        prop = self.propagator
        prop_array = prop.evaluate_propagator_array(
            self.gpts, self.sampling, self.wavelength, dz, self.tilt
        )
        for slice in potential.array:
            out_array = out_array * np.exp(1j * self.sigma * slice)
            out_array = prop.propagate(out_array, prop_array)
        return out_array