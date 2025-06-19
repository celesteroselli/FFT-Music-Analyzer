# Simple pygame program

# Import and initialize the pygame library
import pygame
import fft
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
running = True
y = 250
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
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            y = fft.run("one", True, False)
            print(y)

# Done! Time to quit.
pygame.quit()