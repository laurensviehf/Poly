import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LogLocator, LogFormatterExponent, ScalarFormatter

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Messwerte"

data = ["20_PVP_amp", "20_PVP_frq"]

plt.xlabel("deformation [%]")
plt.ylabel("G'[Pa]")
plt.xscale("log")
plt.yscale("log")
plt.xlim(0.005, 10)

dataAMP = pd.read_csv(allDataPath + "\\" + data[0] + ".csv", sep = ";", decimal = ",")

amplitude = dataAMP["Deformation [%]"].to_numpy(dtype=float)
g1 = dataAMP["Speichermodul [Pa]"].to_numpy(dtype=float)

plt.plot(amplitude, g1)
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "20_PVP_amp_G1")

plt.clf()

plt.xlabel("deformation [%]")
plt.ylabel("G''[Pa]")
plt.xscale("log")
plt.ylim()

amplitude = dataAMP["Deformation [%]"].to_numpy(dtype=float)
g2 = dataAMP["Verlustmodul [Pa]"].to_numpy(dtype=float)

plt.plot(amplitude, g2)
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "20_PVP_amp_G2")


plt.clf()

plt.xlabel("deformation [%]")
plt.ylabel("|$\eta$*| [Pa $\cdot$ s] ")
plt.xscale("log")
plt.ylim()

amplitude = dataAMP["Deformation [%]"].to_numpy(dtype=float)
eta = dataAMP["Betrag(Viskosität) [Pa·s]"].to_numpy(dtype=float)

plt.plot(amplitude, eta)

plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "20_PVP_amp_eta")