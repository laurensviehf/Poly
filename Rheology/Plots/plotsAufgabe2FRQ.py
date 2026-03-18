import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LogLocator, LogFormatterExponent, ScalarFormatter

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Messwerte"

data = ["20_PVP_amp", "20_PVP_frq"]

plt.xlabel("$\omega$ [$s^{-1}$]")
plt.ylabel("|$\eta$*| [Pa $\cdot$ s]")
plt.xscale("log")


dataFRQ = pd.read_csv(allDataPath + "\\" + data[1] + ".csv", sep = ";", decimal = ",")

g1 = dataFRQ["Speichermodul [Pa]"].to_numpy(dtype = float)
g2 = dataFRQ["Verlustmodul [Pa]"].to_numpy(dtype = float)
tanDelta = dataFRQ["Betrag(Viskosität) [Pa·s]"]

frequenz = dataFRQ["Kreisfrequenz [1/s]"]

plt.plot(frequenz, tanDelta)
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "20_PVP_frq_betragEta")

plt.clf()

plt.xlabel("$\omega$ [$s^{-1}$]")
plt.ylabel("G' or G'' [Pa]")
plt.xscale("log")
plt.yscale("log")

plt.plot(frequenz, g1)
plt.plot(frequenz, g2)

plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "20_PVP_frq_G1_G2")