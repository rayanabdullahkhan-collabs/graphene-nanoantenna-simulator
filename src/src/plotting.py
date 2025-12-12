import matplotlib.pyplot as plt


def plot_spectrum(freqs_thz, absorption, title="Absorption Spectrum"):
    plt.figure()
    plt.plot(freqs_thz, absorption)
    plt.xlabel("Frequency (THz)")
    plt.ylabel("Absorption")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
