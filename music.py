import pygame
import time
import numpy as np
from pysinewave import SineWave
from pysinewave import utilities
import fft

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