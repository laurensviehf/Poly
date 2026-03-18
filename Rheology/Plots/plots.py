import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Messwerte\"

lampDataPath = r""
filterDataPath = r""

bandDataPath = r""
bandTransmissionDataPath = r""

allData = pd.read_csv(allDataPath, sep = ';', decimal=',', dtype=float)
rawData = pd.read_csv(rawDataPath, sep = ';', decimal=',', dtype=float)

lampData = pd.read_csv(lampDataPath, sep =';', decimal = ',', dtype= float)
filterData = pd.read_csv(filterDataPath, sep =';', decimal = ',', dtype= float)

bandData = pd.read_csv(bandDataPath, sep = ';', decimal=',', dtype=float)
bandTransmission = pd.read_csv(bandTransmissionDataPath, sep = ';', decimal=',', dtype=float)

