import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import music21 as music
from scipy.signal import find_peaks

#classifying notes

noteslist = []

c3 = music.note.Note("C3")
noteslist.append(c3)
csharp3 = music.note.Note("C#3")
noteslist.append(csharp3)
d3 = music.note.Note("D3")
noteslist.append(d3)
dsharp3 = music.note.Note("D#3")
noteslist.append(dsharp3)
e3 = music.note.Note("E3")
noteslist.append(e3)
f3 = music.note.Note("F3")
noteslist.append(f3)
fsharp3 = music.note.Note("F#3")
noteslist.append(fsharp3)
g3 = music.note.Note("G3")
noteslist.append(g3)
gsharp3 = music.note.Note("G#3")
noteslist.append(gsharp3)
a3 = music.note.Note("A3")
noteslist.append(a3)
asharp3 = music.note.Note("A#3")
noteslist.append(asharp3)
b3 = music.note.Note("B3")
noteslist.append(b3)

c4 = music.note.Note("C4")
noteslist.append(c4)
csharp4 = music.note.Note("C#4")
noteslist.append(csharp4)
d4 = music.note.Note("D4")
noteslist.append(d4)
dsharp4 = music.note.Note("D#4")
noteslist.append(dsharp4)
e4 = music.note.Note("E4")
noteslist.append(e4)
f4 = music.note.Note("F4")
noteslist.append(f4)
fsharp4 = music.note.Note("F#4")
noteslist.append(fsharp4)
g4 = music.note.Note("G4")
noteslist.append(g4)
gsharp4 = music.note.Note("G#4")
noteslist.append(gsharp4)
a4 = music.note.Note("A4")
noteslist.append(a4)
asharp4 = music.note.Note("A#4")
noteslist.append(asharp4)
b4 = music.note.Note("B4")
noteslist.append(b4)

c5 = music.note.Note("C5")
noteslist.append(c5)
csharp5 = music.note.Note("C#5")
noteslist.append(csharp5)
d5 = music.note.Note("D5")
noteslist.append(d5)
dsharp5 = music.note.Note("D#5")
noteslist.append(dsharp5)
e5 = music.note.Note("E5")
noteslist.append(e5)
f5 = music.note.Note("F5")
noteslist.append(f5)
fsharp5 = music.note.Note("F#5")
noteslist.append(fsharp5)
g5 = music.note.Note("G5")
noteslist.append(g5)
gsharp5 = music.note.Note("G#5")
noteslist.append(gsharp5)
a5 = music.note.Note("A5")
noteslist.append(a5)
asharp5 = music.note.Note("A#5")
noteslist.append(asharp5)
b5 = music.note.Note("B5")
noteslist.append(b5)

#starting audio processing

factor = 2**17

sound = AudioSegment.from_file('500.wav')
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

#get peaks using scipy

average = np.sum(np.abs(frequencylist)[1:intervals//2])/(intervals/2)

m_peaks = find_peaks(np.abs(frequencylist)[1:intervals//2], height=average*50, distance = 50)

peakindex = []

for x in m_peaks[0]:
    itemindex = freq_axis[x]
    peakindex.append(itemindex)

#find notes based on peaks (with hz differences):

finalnotes = []

for note in peakindex:
    min_diff = 2000
    closest_note = None
    actual_diff = 0
    sharp = False

    for x in noteslist:
        freq = x.pitch.frequency
        if (np.abs(note-freq)<min_diff):
            #print(str(np.abs(note-freq)) + " < " + str(min_diff))
            closest_note = x
            actual_diff = note-freq
            min_diff = np.abs(note-freq)
            if note-freq > 0:
                sharp = True
            else:
                sharp = False

    msg = "sharp" if sharp else "flat"
    if (np.abs(actual_diff) < 50):
        finalnotes.append(closest_note.name + " : " + str(np.abs(actual_diff)) + " " + msg)

print(finalnotes)