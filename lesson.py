import pygame
from usersettings import *
from physics import WINDOW_SIZE
from pygame_markdown import MarkdownRenderer

class MutableInt:
    def __init__(self, value):
        self.value = value

    def increment(self, value):
        self.value += value

    def __str__(self):
        return str(self.value)

def lesson_content(unit, level):
    md = MarkdownRenderer()
    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson1.md")
    global count
    count = MutableInt(1)
    display = pygame.Surface(WINDOW_SIZE)
    md.set_area(display, 1, 1)
    return md, display, count, unit, level

def do_lesson(display, md, pygame_events, mouse_x, mouse_y, mouse_pressed):
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
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