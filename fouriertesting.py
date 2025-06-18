import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import math
from scipy.integrate import quad
from pydub import AudioSegment
import cmath

duration = 10 #duration time that the wave should go for
maxfreq = 50 #max frequency. i.e., how far does the graph over frequency go

def wave(x):
    return (math.cos(2*math.pi*x*30) + math.cos(2*math.pi*x*20))

def circle(x, f):
    term = f * 2 * math.pi
    z = complex(math.cos(term*x), math.sin(term*x))
    return z

def integrate(f):
    #integrating the fourier function over the entire duration of the wave
    return sp.integrate.quad(lambda x: wave(x) * cmath.exp(-2j * math.pi * f * x), 0, duration, limit=1000, complex_func=True)[0]

def fourier(x, f):
    #returns a complex number for where the point is
    return circle(x, f)*wave(x)

fig, ax = plt.subplots()

x = []
y = []

freqdistance = np.linspace(0, maxfreq, 2000)

for i in freqdistance:
    x.append(i)
    y.append(integrate(i))
    #y.append(wave(f))

ax.plot(x, y)
plt.show()

#there should be peaks at around 2 and 4
peaks = []

average = (np.average(y)).real

complete = False
counter = 0
while not complete:
    #get max of y values
    ymax = np.max(y) 

    #get index of that max
    index = y.index(ymax)

    #IF it's above 1 above the average, then get freq from index of x, and add
    if (ymax > average*10):
        freq = x[index]
        peaks.append(freq)

        #then, get rid of value and 20 surrounding values in y and x

        for i in range(40):
            y[-20 + index + i] = 0
            x[-20 + index + i] = 0

        counter = counter + 1
    else:
        complete = True

    if (counter > 10):
        complete = True

print(peaks)