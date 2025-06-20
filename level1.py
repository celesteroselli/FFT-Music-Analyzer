# Simple pygame program

# Import and initialize the pygame library
import pygame
import fft
import time
from pysinewave import SineWave
import numpy as np

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
threshold = 20

# Run until the user asks to quit
running = True
y = 261.3
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 500-y), 75)

    # Flip the display
    pygame.display.flip()
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            sine_wave = SineWave(pitch=0, pitch_per_second=0)

            # Play the sine wave
            sine_wave.play()

            # Keep playing for 2 seconds
            time.sleep(2)

            # Stop the sine wave
            sine_wave.stop()
            print(y)
            y = fft.run("one", True, False)
            diff = np.abs(261.3*(5/4) - y)
            msg = "sharp" if (261.3*(5/4) - y < 0) else "flat"
            if diff > threshold:
                print(f"oop, sorry, you were {diff} hz {msg}")
            else:
                print("congrats!")

# Done! Time to quit.
pygame.quit()