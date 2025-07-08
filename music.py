import pygame
import time
import numpy as np
from pysinewave import SineWave
from pysinewave import utilities
import Fourier.fft as fft
import music21
from Fourier.usersettings import *

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
    run = fft.run("one", True, False, 0)
    y = run[0]
    print("y =" + str(y))
    diff = np.abs(pitch*(interval) - y)
    msg = "sharp" if (pitch*(interval) - y < 0) else "flat"
    if diff > threshold:
        message = f"sorry, you were {diff} hz {msg}"
        return False, y, run[1], message
    else:
        print("congrats!")
        return True, y, run[1]
    
def constraint(pitch, pitch2):
    if pitch2 < pitch:
        higher = pitch
        lower = pitch2
    else:
        higher = pitch2
        lower = pitch
    
    print("sing a major third above the pitch")
    sine_wave = SineWave(pitch=1, pitch_per_second=500)
    sine_wave2 = SineWave(pitch=1, pitch_per_second=500)
    sine_wave.set_frequency(lower)
    sine_wave2.set_frequency(higher)
    # Play the sine wave
    sine_wave.play()

    # Keep playing for 2 seconds
    time.sleep(2)
    sine_wave.stop()
    
    sine_wave2.play()
    
    time.sleep(2)

    # Stop the sine wave
    sine_wave2.stop()
    run = fft.run("one", True, False, 0)
    y = run[0]
    print("y =" + str(y))
    if (y > lower) and (y < higher):
        return True, y, run[1]
    else:
        return False, y, run[1]

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
    run = fft.run("one", True, False, 0)
    y = run[0]
    return y, run[1]

def hit_rhythms(max):
    list = fft.run("rhythm", True, False, max)
    return list

def chord(num, type):
    octavedown = 1
    print("play a major chord")
    pitch = music21.pitch.Pitch(num).frequency
    if pitch>=(music21.pitch.Pitch("F").frequency):
        pitch = pitch/2
        octavedown = 2
    sine_wave = SineWave(pitch=1, pitch_per_second=500)
    sine_wave.set_frequency(pitch)
    
    if type=="switch-to-m":
        sine_wave.play()
        time.sleep(1)
        i = music21.interval.Interval("M3")
        i.noteStart = music21.note.Note(num)
        M3 = i.noteEnd
        sine_wave.set_frequency(M3.pitch.frequency/octavedown)
        time.sleep(1)
        i = music21.interval.Interval("P5")
        i.noteStart = music21.note.Note(num)
        M3 = i.noteEnd
        sine_wave.set_frequency(M3.pitch.frequency/octavedown)
        time.sleep(1)
        sine_wave.stop()
    elif type=="switch-to-M":
        sine_wave.play()
        time.sleep(1)
        i = music21.interval.Interval("m3")
        i.noteStart = music21.note.Note(num)
        M3 = i.noteEnd
        sine_wave.set_frequency(M3.pitch.frequency/octavedown)
        time.sleep(1)
        i = music21.interval.Interval("P5")
        i.noteStart = music21.note.Note(num)
        M3 = i.noteEnd
        sine_wave.set_frequency(M3.pitch.frequency/octavedown)
        time.sleep(1)
        sine_wave.stop()
    else:
        # Play the sine wave
        sine_wave.play()

        # Keep playing for 2 seconds
        time.sleep(2)

        # Stop the sine wave
        sine_wave.stop()
    
    notes = []
    
    match type:
        case "major":
            i = music21.interval.Interval("M3")
            i2 = music21.interval.Interval("P5")
        case "minor":
            i = music21.interval.Interval("m3")
            i2 = music21.interval.Interval("P5")
        case "switch-to-m":
            i = music21.interval.Interval("m3")
            i2 = music21.interval.Interval("P5")
        case "switch-to-M":
            i = music21.interval.Interval("M3")
            i2 = music21.interval.Interval("P5")
        case _:
            i = music21.interval.Interval("M3")
            i2 = music21.interval.Interval("P5")
        
    i.noteStart = music21.note.Note(num)
    i2.noteStart = music21.note.Note(num)
    M3 = i.noteEnd
    P5 = i2.noteEnd
    
    test_chord = [num, M3.name, P5.name]
    
    run = fft.run("all", True, False, 0)
    notes = run[0]
    fig = run[1]

    pitches = []
    for x in notes:
        pitches.append(x.name)
    
    Found = 0
    for x in test_chord:
        for y in pitches:
            if music21.pitch.Pitch(y).isEnharmonic(music21.pitch.Pitch(x)):
                print(f"{x} is in pitches, as {x} is enharmonic to {y}")
                Found = Found + 1
                
    if (Found < len(test_chord)):
        return False, fig, f"sorry, you sang {pitches} while looking for {test_chord}"
        
    others = []
    for y in pitches:
        if y not in test_chord:
            others.append(y)
    
    if others:
        return True, fig, f"you sang {test_chord} with over/under-tones {others}"
    else:
        return True, fig, f"you sang {test_chord} with no over/under-tones"