# -------------------------------------------------------- #
# created by ShakedKod for the Oort Studios | Project Time #
# https://OortStudios.github.io/ProjectTime/               #
# -------------------------------------------------------- #
import os

try:
    import pygame
    from moviepy.editor import *
    from pygame.locals import *
except:
    try:
        os.system("pip install pygame")
        os.system("pip install moviepy")
        import pygame
        from moviepy.editor import *
        from pygame.locals import *
    except:
        try:
            os.system("pip3 install pygame")
            os.system("pip3 install moviepy")
            import pygame
            from moviepy.editor import *
            from pygame.locals import *
        except:
            try:
                os.system("py -m pip install pygame")
                os.system("py -m pip install moviepy")
                import pygame
                from moviepy.editor import *
                from pygame.locals import *
            except:
                try:
                    os.system("py3 -m pip install pygame")
                    os.system("py3 -m pip install moviepy")
                    import pygame
                    from moviepy.editor import *
                    from pygame.locals import *
                except:
                    print("The pygame and moviepy modules are not installed. Please install them and try again.")

from .sounds      import Sounds
from .cutsences   import Cutscence
from .application import Application

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