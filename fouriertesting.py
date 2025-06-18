import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import math
from scipy.integrate import quad
from pydub import AudioSegment

maxfreq = 800

# sound = AudioSegment.from_file('sound1.wav')
# sound = sound.set_frame_rate(maxfreq)
# samples = sound.get_array_of_samples()
# arraysamples = np.array(samples)
# print(arraysamples.size)

global f
f = 0.1

def wave(x):
    return (math.cos(2*math.pi*x) + math.cos(2*math.pi*x*2))

def circle(x):
    term = f * 2 * math.pi
    z = complex(math.cos(term*x), math.sin(term*x))
    return z

flist = np.linspace(0, 2*math.pi, 200)

def integrate():
    #goes through a full circle and integrates the fourier curve
    return sp.integrate.quad(fourier, 0, 2*math.pi, complex_func=True)

def fourier(x):
    #returns a complex number for where the point is
    #return circle(x)*arraysamples[int(x)]
    return circle(x)*wave(x)

fig, ax = plt.subplots()

x = []
y = []

for i in flist:
    #setting 
    f = i
    x.append(f)
    y.append(integrate()[0])
    #y.append(wave(f))

ax.plot(x, y)
plt.show()

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
    if (ymax > average*2):
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

