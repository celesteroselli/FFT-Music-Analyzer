import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

factor = 2**17

sound = AudioSegment.from_file('domeso3.wav')
audsamples = sound.get_array_of_samples()
middle = len(audsamples)//2

#TODO: get sample size working!!!!!
samples = np.array(audsamples[(middle-(factor//2)):(middle+(factor//2))])
#window = np.hanning(len(samples))
#samples = samples * window
Fs = sound.frame_rate

#MUST BE A FACTOR OF TWO
intervals = factor

xvals = np.linspace(0, 2*np.pi, intervals)
#samples = np.sin(300*xvals)+np.sin(100*xvals)

#should go to 2
frequencies = []

#max frequency is N/2, so test all frequencies until N/2

print("\n \n \n \n \n")

distance = xvals[1]-xvals[0]

#x is terms
def split(x):
    N = len(x)
    if (N==1):
        #exponent will be 1 bc e^0 = 1
        return x
    else:
        x_even = split(x[::2]) #all even-ordered elements (step of 2 starting at 0)
        x_odd = split(x[1::2]) #all odd-ordered elements (step of 2 starting at 1)

        #RECURSION WILL FINISH ONCE BOTH EVEN AND ODD ARE RETURNED WITH THE SUM OF THE TWO BRANCHES

        #now that you have final sums:
        
        m_list = [0] * N
        for k in range(N//2):
            exp = np.exp((-2j * np.pi * k)/N)

            m_list[k] = (x_even[k] + exp*x_odd[k])
            m_list[k + N//2] = x_even[k] - exp*x_odd[k]
        return m_list

freq_axis = [0] * (intervals)
freq_axis = [(Fs * k) / intervals for k in range(intervals)]

frequencylist = split(samples)

plt.plot(freq_axis[1:intervals//2], (np.abs(frequencylist)[1:intervals//2]))
plt.xlim(0, 1000)
plt.show()
