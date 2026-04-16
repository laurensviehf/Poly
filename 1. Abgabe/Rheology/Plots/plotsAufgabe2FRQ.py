import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LogLocator, LogFormatterExponent, ScalarFormatter

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Messwerte"

data = ["20_PVP_amp", "20_PVP_frq"]

plt.xlabel("$\omega$ [$s^{-1}$]")
plt.ylabel("|$\eta$*| [Pa $\cdot$ s]")
plt.xscale("log")
plt.yscale("log")


dataFRQ = pd.read_csv(allDataPath + "\\" + data[1] + ".csv", sep = ";", decimal = ",")

g1 = dataFRQ["Speichermodul [Pa]"].to_numpy(dtype = float)
g2 = dataFRQ["Verlustmodul [Pa]"].to_numpy(dtype = float)
tanDelta = dataFRQ["Betrag(Viskosität) [Pa·s]"]

frequenz = dataFRQ["Kreisfrequenz [1/s]"]

plt.plot(frequenz, tanDelta, marker = "o")
plt.tight_layout()
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Bilder\20_PVP_frq_betragEta.png")
plt.show()


plt.clf()

plt.xlabel("$\omega$ [$s^{-1}$]")
plt.ylabel("G' or G'' [Pa]")
plt.xlim(1, 10e1)
plt.xscale("log")
plt.yscale("log")

plt.plot(frequenz, g1, label = "G'", marker = "o")
plt.plot(frequenz, g2, label = "G''", marker = "o")
plt.legend()
plt.tight_layout()
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Bilder\20_PVP_frq_G1_G2.png")
plt.show()
