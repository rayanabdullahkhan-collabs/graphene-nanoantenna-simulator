from model import GrapheneNanoAntennaModel
from plotting import plot_spectrum


def main():
    model = GrapheneNanoAntennaModel(patch_length_um=30.0, n_eff=3.0, peak_absorption=0.9, Q=25.0)
    print(f"Estimated resonance frequency: {model.f0_thz:.2f} THz")

    freqs, absorption = model.sweep_frequency(f_min_thz=0.1, f_max_thz=5.0, num_points=1500)
    plot_spectrum(freqs, absorption, title="Graphene Patch Nanoantenna Absorption Spectrum")


if __name__ == "__main__":
    main()
