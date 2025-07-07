import pygame
from usersettings import *
from physics import WINDOW_SIZE
from pygame_markdown import MarkdownRenderer
import gif_pygame

class MutableInt:
    def __init__(self, value):
        self.value = value

    def increment(self, value):
        self.value += value

    def __str__(self):
        return str(self.value)

def lesson_content(unit, level, is_gif):
    md = MarkdownRenderer()
    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson1.md")
    if is_gif:
        image = gif_pygame.load(f"lessons/{unit}/{level}/image.gif")
        gif = gif_pygame.GIFPygame([(image, 1)])
    else:
        image = gif_pygame.load(f"lessons/{unit}/{level}/image.png")
        gif = gif_pygame.GIFPygame([(image, 1)])
    global count
    count = MutableInt(1)
    display = pygame.Surface(WINDOW_SIZE)
    md.set_area(display, 1, 1)
    return md, display, count, unit, level, image

def do_lesson(display, md, pygame_events, mouse_x, mouse_y, mouse_pressed, image):
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
    #display.blit(image,((WINDOW_SIZE[0]-image.get_width())/2, WINDOW_SIZE[1]-image.get_height()-100))
    image.render(display, ((WINDOW_SIZE[0]-700, WINDOW_SIZE[1]-700)))
    #display.blit(image.blit_ready(), ((WINDOW_SIZE[0]-100, WINDOW_SIZE[1]-100)))
    # text = my_font.render(content, True, (0,255,0), (0,0,128))
    # textRect = text.get_rect()
    
    # display.fill((0,0,100))
    # display.blit(text, textRect)
    pygame.display.update()
    return display

def inputs(events, md, count, isdone, unit, level):
    for event in events:
        if ((event.type == pygame.KEYDOWN)):
            if event.key == pygame.K_LEFT: 
                if (count.value > 1):
                    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson{count.value-1}.md")
                    count.increment(-1)
            if event.key == pygame.K_RIGHT:
                if (count.value < 3):
                    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson{count.value+1}.md")
                    count.increment(1)
                else:
                    print("finished!")
                    isdone.increment(1)
                    print(isdone.value)