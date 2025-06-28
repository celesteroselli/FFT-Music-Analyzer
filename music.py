import pygame
import time
import numpy as np
from pysinewave import SineWave
from pysinewave import utilities
import fft
import music21
from usersettings import *

global y
y = utilities.pitch_to_frequency(3)
threshold = 20
factor = 1.2

def harmonize(pitch, interval):
    print("sing a major third above the pitch")
    sine_wave = SineWave(pitch=1, pitch_per_second=500)
    sine_wave.set_frequency(pitch)
    # Play the sine wave
    sine_wave.play()

    # Keep playing for 2 seconds
    time.sleep(2)

    # Stop the sine wave
    sine_wave.stop()
    y = fft.run("one", True, False, 0)
    print("y =" + str(y))
    diff = np.abs(pitch*(interval) - y)
    msg = "sharp" if (pitch*(interval) - y < 0) else "flat"
    if diff > threshold:
        print(f"oop, sorry, you were {diff} hz {msg}")
        return False, y, f"oop, sorry, you were {diff} hz {msg}"
    else:
        print("congrats!")
        return True, y, "congrats!"

def pitch(pitch):
    print("sing a major third above the pitch")
    sine_wave = SineWave(pitch=1, pitch_per_second=500)
    sine_wave.set_frequency(pitch)
    # Play the sine wave
    sine_wave.play()

    # Keep playing for 2 seconds
    time.sleep(2)

    # Stop the sine wave
    sine_wave.stop()
    y = fft.run("one", True, False, 0)
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
    
    base = pitch_data["Note"][pitchnum]
    print("base = " + base)
    
    notes = fft.run("all", True, False, 0)
    
    final_chord = []
    
    for x in notes:
        if ((x.pitch.frequency > USER_CHORD_MIN) and (x.pitch.frequency < USER_CHORD_MAX)):
            if x.name != None:
                print(x.name)
                final_chord.append(x.name)
                    
    myChord = music21.chord.Chord(final_chord)
    print(myChord)
    print(myChord.pitchedCommonName)
    
    if (myChord.pitchedCommonName==f"{base}-major triad") or (myChord.pitchedCommonName==f"enharmonic equivalent to {base}-major triad"):
        print("that's c major!!")
        return True
    else: 
        print("oop that's not right")
        return False