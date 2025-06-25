# Simple pygame program

# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from dialogue import dialogue_actions

def level_run(num):

    pygame.font.init() # you have to call this at the start, 
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    from level1copy import Level_1

    pygame.init()

    running = True

    m_player = PlayerClass(PLAYER_SCREEN_OFFSET, 10, 100, 100)
    camera = Camera(m_player)
    follow = CamScroll(camera, m_player)

    #GET THE CURRENT LEVEL:::::

    current_level = Level_1

    current_level.setup(camera)

    #END GETTING CURRENT LEVEL:::::

    #dialogue variables
    current_level.variables["dialogue_on"] = False
    current_level.variables["new_dialogue"] = True
    dialogue_box = pygame.Rect(100, WINDOW_SIZE[1]-100, WINDOW_SIZE[0]-200, 50)
    current_level.variables["dialogue_count"] = 0
    write = ""
    dialogue_box = pygame.Rect(100, WINDOW_SIZE[1]-100, WINDOW_SIZE[0]-200, 50)

    #clock starts
    clock = pygame.time.Clock()

    #start the run loop
    while running:
    
        if (not current_level.variables["dialogue_on"]):
            #freezes screen if dialogue!
            handle_move(m_player)
            draw_background(camera, m_player, current_level.variables["foreground"], current_level.game_map)
            m_player.draw(display, camera)
            follow.scroll()
        else:
            if (current_level.variables["new_dialogue"]):
                #handling dialogue display stuff
                print("writing text")
                pygame.draw.rect(display, (0, 255, 0), dialogue_box)
                text_surface = my_font.render(write, False, (0,0,255), None)
                display.blit(text_surface,(dialogue_box.x,dialogue_box.y))
                current_level.variables["new_dialogue"] = False
            
        write = dialogue_actions(current_level.variables)
    
        #get always game events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
            if ((event.type == pygame.KEYDOWN) and (current_level.variables["dialogue_on"]==True)):
                if event.key == pygame.K_ESCAPE: 
                    print("pressed escape")
                    current_level.variables["dialogue_on"] = False
                    current_level.variables["new_dialogue"] = True
                    current_level.variables["dialogue_count"] += 1
            
        current_level.inputs(events)             
            
        screen.blit(display, (0,0))
        pygame.display.update()
        clock.tick(130)

    # Quit the run loop when it's done
    pygame.quit()
    return True

level_run(1)