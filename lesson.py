import pygame
from usersettings import *
from physics import WINDOW_SIZE
from pygame_markdown import MarkdownRenderer
import gif_pygame
import os

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
    if is_gif==0:
        image = gif_pygame.load(f"lessons/{unit}/{level}/image.gif")
        scaledown = 400/image.get_height()
        gif_pygame.transform.scale_by(image, scaledown)
        gif = gif_pygame.GIFPygame([(image, 1)])
    elif is_gif==1:
        image = gif_pygame.load(f"lessons/{unit}/{level}/image.png")
        scaledown = 400/image.get_height()
        gif_pygame.transform.scale_by(image, scaledown)
        gif = gif_pygame.GIFPygame([(image, 1)])
    else:
        image = False
    global count
    count = MutableInt(1)
    display = pygame.Surface(WINDOW_SIZE)
    md.set_area(display, 1, 1)
    return md, display, count, unit, level, image

def do_lesson(display, md, pygame_events, mouse_x, mouse_y, mouse_pressed, image):
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)
    #display.blit(image,((WINDOW_SIZE[0]-image.get_width())/2, WINDOW_SIZE[1]-image.get_height()-100))
    if image != False:
        image.render(display, ((WINDOW_SIZE[0]-image.get_width())/2, (WINDOW_SIZE[1]-image.get_height()-100)))
    #display.blit(image.blit_ready(), ((WINDOW_SIZE[0]-100, WINDOW_SIZE[1]-100)))
    # text = my_font.render(content, True, (0,255,0), (0,0,128))
    # textRect = text.get_rect()
    
    # display.fill((0,0,100))
    # display.blit(text, textRect)
    md.set_line_gaps(gap_line=8, gap_paragraph=70)
    md.set_color_hline(r=255, g=255, b=255)  # default values
    md.set_color_background(r=5, g=43, b=87)
    md.set_font_sizes(h1=40, h2=32, h3=32, text=25, code=25, quote=25)  # these are the default values
    pygame.display.update()
    return display

def inputs(events, md, count, isdone, unit, level):
    length = len(os.listdir(f'lessons/{unit}/{level}/'))
    print("length =", length)
    
    for event in events:
        if ((event.type == pygame.KEYDOWN)):
            if event.key == pygame.K_LEFT: 
                if (count.value > 1):
                    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson{count.value-1}.md")
                    count.increment(-1)
            if event.key == pygame.K_RIGHT:
                if (count.value < length-1):
                    md.set_markdown(mdfile_path=f"lessons/{unit}/{level}/lesson{count.value+1}.md")
                    count.increment(1)
                else:
                    count = 0
                    print("finished!")
                    isdone.increment(1)
                    print(isdone.value)