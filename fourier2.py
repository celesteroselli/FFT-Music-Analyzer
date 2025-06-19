import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import math
from scipy.integrate import quad
from pydub import AudioSegment

maxfreq = 800
rate = 200

sound = AudioSegment.from_file('sound.wav')
sound = sound.set_frame_rate(rate)
samples = sound.get_array_of_samples()
arraysamples = np.array(samples)

global f
f = 0.1

def wave(x):
    return (math.cos(2*math.pi*x) + math.cos(2*math.pi*x*7))

flist = np.linspace(0, 30, rate)

def integrate():
    #goes through a full circle and integrates the fourier curve
    return sp.integrate.quad(fourier, 0, 2*math.pi, complex_func=True)

def fourier(x):
    #returns a complex number for where the point is
    return wave(x)*np.exp(-2j * np.pi * f * x)

fig, ax = plt.subplots()

x = []
y = []

for i in flist:
    #setting 
    f = i
    x.append(f)
    y.append(fourier(f))
    #y.append(wave(f))

ax.plot(x, y)
plt.show()

