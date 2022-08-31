from tkinter import *
import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk , Image
import PIL
import cv2
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
data=pd.read_csv("C:/Users/user/Desktop/웹 프로그래밍/이건파이썬이여/AL_SAMPLE_1.csv")

stress=data["Tensile stress"].to_numpy()
Disp=data["Displacement"].to_numpy()


strain=Disp/8.25

fig,ax1=plt.subplots()

ax1.plot(strain,stress)