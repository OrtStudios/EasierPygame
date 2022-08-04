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
from .base        import *