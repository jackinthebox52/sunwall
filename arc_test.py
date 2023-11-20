'''Experimenting to develop a function for generating an arc across images of varios sizes'''
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

W = 1920
H = 1080

def f(x, w, h):
    a = 1 / (w * 1.5) #Calculate the arc's scale based on the image width
    return -(a)*(x-(w/2))**2 + (h*0.9) #Return the y-value of the arc at point x

x = np.linspace(1, W, 100)

plt.plot(x, f(x, W, H), color='red')
plt.xlim(0, W)
plt.ylim(0, H)
plt.show()