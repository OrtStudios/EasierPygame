import pygame
from pygame.locals import *

def initPygame() -> None:
    """
    Initializes pygame.
    """
    pygame.init()
    pygame.display.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    pygame.mixer.init() #init pygame mixer
    pygame.display.init() #init pygame display

# exit pygame and close the window
def quit() -> None:
    pygame.quit()
    exit("The program has been closed.")

from . import entities as Entity