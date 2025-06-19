import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import music21 as music
import wavio as wv
from scipy.signal import find_peaks
import sounddevice as sd

recording = True
sound_input = 'output.wav'

def record():
    fs = 66000  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    wv.write(sound_input, myrecording, fs, sampwidth=2)

def setup():
    global notes_list
    notes_list = []
    
    print("\n\n\n\n\n")
    c3 = music.note.Note("C3")
    notes_list.append(c3)
    csharp3 = music.note.Note("C#3")
    notes_list.append(csharp3)
    d3 = music.note.Note("D3")
    notes_list.append(d3)
    dsharp3 = music.note.Note("D#3")
    notes_list.append(dsharp3)
    e3 = music.note.Note("E3")
    notes_list.append(e3)
    f3 = music.note.Note("F3")
    notes_list.append(f3)
    fsharp3 = music.note.Note("F#3")
    notes_list.append(fsharp3)
    g3 = music.note.Note("G3")
    notes_list.append(g3)
    gsharp3 = music.note.Note("G#3")
    notes_list.append(gsharp3)
    a3 = music.note.Note("A3")
    notes_list.append(a3)
    asharp3 = music.note.Note("A#3")
    notes_list.append(asharp3)
    b3 = music.note.Note("B3")
    notes_list.append(b3)

    c4 = music.note.Note("C4")
    notes_list.append(c4)
    csharp4 = music.note.Note("C#4")
    notes_list.append(csharp4)
    d4 = music.note.Note("D4")
    notes_list.append(d4)
    dsharp4 = music.note.Note("D#4")
    notes_list.append(dsharp4)
    e4 = music.note.Note("E4")
    notes_list.append(e4)
    f4 = music.note.Note("F4")
    notes_list.append(f4)
    fsharp4 = music.note.Note("F#4")
    notes_list.append(fsharp4)
    g4 = music.note.Note("G4")
    notes_list.append(g4)
    gsharp4 = music.note.Note("G#4")
    notes_list.append(gsharp4)
    a4 = music.note.Note("A4")
    notes_list.append(a4)
    asharp4 = music.note.Note("A#4")
    notes_list.append(asharp4)
    b4 = music.note.Note("B4")
    notes_list.append(b4)

    c5 = music.note.Note("C5")
    notes_list.append(c5)
    csharp5 = music.note.Note("C#5")
    notes_list.append(csharp5)
    d5 = music.note.Note("D5")
    notes_list.append(d5)
    dsharp5 = music.note.Note("D#5")
    notes_list.append(dsharp5)
    e5 = music.note.Note("E5")
    notes_list.append(e5)
    f5 = music.note.Note("F5")
    notes_list.append(f5)
    fsharp5 = music.note.Note("F#5")
    notes_list.append(fsharp5)
    g5 = music.note.Note("G5")
    notes_list.append(g5)
    gsharp5 = music.note.Note("G#5")
    notes_list.append(gsharp5)
    a5 = music.note.Note("A5")
    notes_list.append(a5)
    asharp5 = music.note.Note("A#5")
    notes_list.append(asharp5)
    b5 = music.note.Note("B5")
    notes_list.append(b5)

def process_audio():

    #must be a factor of 2
    factor = 2**17

    sound = AudioSegment.from_file(sound_input)
    aud_samples = sound.get_array_of_samples()
    middle = len(aud_samples)//2

    #TODO: get sample size working!!!!!
    global samples
    samples = np.array(aud_samples[(middle-(factor//2)):(middle+(factor//2))])

    global intervals
    intervals = factor
    
    global Fs
    Fs = sound.frame_rate
def split(x):
    N = len(x)
    if (N==1):
        #exponent will be 1 bc e^0 = 1
        return x
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

def plot():

    freq_axis = [0] * (intervals)
    freq_axis = [(Fs * k) / intervals for k in range(intervals)]

    frequency_list = split(samples)

    plt.plot(freq_axis[1:intervals//2], (np.abs(frequency_list)[1:intervals//2]))
    plt.xlim(0, 1000)
    plt.show()

    #get peaks using scipy

    average = np.sum(np.abs(frequency_list)[1:intervals//2])/(intervals/2)

    m_peaks = find_peaks(np.abs(frequency_list)[1:intervals//2], height=average*50, distance = 50)

    peak_index = []

    for x in m_peaks[0]:
        item_index = freq_axis[x]
        peak_index.append(item_index)

    #find notes based on peaks (with hz differences):

    final_notes = []

    for note in peak_index:
        min_diff = 2000
        closest_note = None
        actual_diff = 0
        sharp = False

        for x in notes_list:
            freq = x.pitch.frequency
            if (np.abs(note-freq)<min_diff):
                #print(str(np.abs(note-freq)) + " < " + str(min_diff))
                closest_note = x
                actual_diff = note-freq
                min_diff = np.abs(note-freq)
                sharp = (note-freq > 0)

        msg = "sharp" if sharp else "flat"
        if (np.abs(actual_diff) < 50):
            final_notes.append(f"{closest_note.name } : {str(np.abs(actual_diff))} {msg}")
    if not final_notes:
        final_notes.append("No note picked up. Please try again!") 
    
    print(final_notes)
    
if (recording):
    record()
setup()
process_audio()
plot()