import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv("AL sapple_1.csv")
stress=data["tensile stress"].to_numpy()
strain=data["Tensile strain (strain 1)"].to_numpy()

ax1.plot(strain,stress)