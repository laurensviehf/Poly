import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Messwerte"
savePath = r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Bilder"

data = ["20_PVP_amp", "20_PVP_frq"]
dataAMP = pd.read_csv(allDataPath + "\\" + data[0] + ".csv", sep=";", decimal=",")

# Gemeinsame Daten extrahieren
amplitude = dataAMP["Deformation [%]"].to_numpy(dtype=float)
g1 = dataAMP["Speichermodul [Pa]"].to_numpy(dtype=float)
g2 = dataAMP["Verlustmodul [Pa]"].to_numpy(dtype=float)
eta = dataAMP["Betrag(Viskosität) [Pa·s]"].to_numpy(dtype=float)

# --- Plot 1: G' ---
plt.figure()
plt.plot(amplitude, g1)
plt.xscale("log")
plt.yscale("log")
plt.xlim(0.005, 10)
plt.xlabel("deformation [%]")
plt.ylabel("G' [Pa]")
plt.savefig(savePath + r"\20_PVP_amp_G1.png")
plt.show()

# --- Plot 2: G'' ---
plt.figure() # Erstellt ein frisches Fenster
plt.plot(amplitude, g2)
plt.xscale("log")
plt.yscale("log")
# plt.ylim() wurde entfernt, da es ohne Argumente die Achsen stören kann
plt.xlabel("deformation [%]")
plt.ylabel("G'' [Pa]")
plt.savefig(savePath + r"\20_PVP_amp_G2.png")
plt.show()

# --- Plot 3: Viskosität ---
plt.figure()
plt.plot(amplitude, eta)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("deformation [%]")
plt.ylabel(r"|$\eta$*| [Pa $\cdot$ s]")
plt.savefig(savePath + r"\20_PVP_amp_eta.png")
plt.show()