import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LogLocator, LogFormatterExponent, ScalarFormatter

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Messwerte"

data = ["ketchup1", "ketchup2", "ketchup3"]

plt.xlabel("Time in $s^{-1}$")
plt.ylabel("shear viscosity $\eta$ [Pa$\cdot$ s]")
plt.yscale("log")


for i in data:
    dataI = pd.read_csv(allDataPath + "\\" + i + ".csv", sep = ";", decimal = ",")

    schubspannung = dataI["Schubspannung [Pa]"].to_numpy(dtype=float)
    viskosität = dataI["Viskosität [Pa·s]"].to_numpy(dtype=float)
    time = dataI["Zeit [s]"]
    plt.plot(time, viskosität)






plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "ketchup")



