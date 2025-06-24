import pygame
import time
import numpy as np
from pysinewave import SineWave
from pysinewave import utilities
import fft
import music21

global y
y = utilities.pitch_to_frequency(3)
threshold = 20

def harmonize(pitchnum, interval):
    print("sing a major third above the pitch")
    sine_wave = SineWave(pitch=pitchnum, pitch_per_second=0)

    # Play the sine wave
    sine_wave.play()

    # Keep playing for 2 seconds
    time.sleep(2)

    # Stop the sine wave
    sine_wave.stop()
    y = fft.run("one", True, False)
    print("y =" + str(y))
    freq = utilities.pitch_to_frequency(pitchnum)
    diff = np.abs(freq*(interval) - y)
    msg = "sharp" if (freq*(interval) - y < 0) else "flat"
    if diff > threshold:
        print(f"oop, sorry, you were {diff} hz {msg}")
    else:
        print("congrats!")
    return y

def hit_rhythms(max):
    list = fft.run("rhythm", True, False, max)
    return list

def chord(pitchnum):
    print("play a major chord")
    sine_wave = SineWave(pitch=pitchnum, pitch_per_second=0)

    # Play the sine wave
    sine_wave.play()

    # Keep playing for 2 seconds
    time.sleep(2)

    # Stop the sine wave
    sine_wave.stop()
    
    notes = []
    
    octave_min = music21.pitch.Pitch("B3").frequency
    octave_max = music21.pitch.Pitch("B4").frequency
    print(octave_min)
    print(octave_max)
    
    notes = fft.run("all", True, False, 0)
    
    final_chord = []
    
    for x in notes:
        if ((x != None) and (x != "")):
            if ((x.pitch.frequency > octave_min) and (x.pitch.frequency < octave_max)):
                if x.name != None:
                    print(x.name)
                    final_chord.append(x.name)
                    
    myChord = music21.chord.Chord(final_chord)
    print(myChord)
    print(myChord.pitchedCommonName)
    
    if (myChord.pitchedCommonName=="C-major triad") or (myChord.pitchedCommonName=="enharmonic equivalent to C-major triad"):
        print("that's c major!!")
        return True
    else: 
        print("oop that's not right")
        return False