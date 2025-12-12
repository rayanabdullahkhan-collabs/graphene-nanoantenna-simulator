import numpy as np

C0 = 3e8  # speed of light (m/s)


class GrapheneNanoAntennaModel:
    """
    Compact resonance model for a graphene patch nanoantenna (THz).
    Toy model for intuition-building (not a full-wave EM solver).
    """

    def __init__(
        self,
        patch_length_um: float = 30.0,
        n_eff: float = 3.0,
        peak_absorption: float = 0.9,
        Q: float = 20.0,
    ) -> None:
        self.patch_length_um = patch_length_um
        self.n_eff = n_eff
        self.peak_absorption = peak_absorption
        self.Q = Q
        self._f0_hz = self._estimate_resonance_frequency_hz()

    def _estimate_resonance_frequency_hz(self) -> float:
        L_m = self.patch_length_um * 1e-6
        return C0 / (2.0 * self.n_eff * L_m)

    @property
    def f0_thz(self) -> float:
        return self._f0_hz * 1e-12

    def absorption_spectrum(self, freqs_thz: np.ndarray) -> np.ndarray:
        f0 = self.f0_thz
        delta_f = f0 / (2.0 * self.Q)
        return self.peak_absorption / (1.0 + ((freqs_thz - f0) / delta_f) ** 2)

    def sweep_frequency(
        self,
        f_min_thz: float = 0.1,
        f_max_thz: float = 5.0,
        num_points: int = 1000,
    ) -> tuple[np.ndarray, np.ndarray]:
        freqs = np.linspace(f_min_thz, f_max_thz, num_points)
        return freqs, self.absorption_spectrum(freqs)
