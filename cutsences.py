import pygame
from moviepy.editor import *
from pygame.locals import *

class Cutscence:

    @staticmethod
    def regular(name: str, path: str, window: pygame.Surface) -> pygame.Surface:
        #%start%------------------------------------%start%#
        pygame.display.set_caption(name)

        screen_resolution: tuple(int, int) = (window.get_width(), window.get_height())

        # check if the window is resizable
        is_resizable: bool = window.get_flags() & pygame.RESIZABLE

        clip = VideoFileClip(
            path,
            has_mask = False,
            audio = True,
            target_resolution = screen_resolution
            )
        clip.preview()

        #reload mixer
        pygame.mixer.quit()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.set_num_channels(64)
        pygame.mixer.init()

        #display
        pygame.display.set_caption(window_name)

        if is_resizable:
            window = pygame.display.set_mode(screen_resolution, pygame.RESIZABLE)
        else:
            window = pygame.display.set_mode(screen_resolution)
        
        return window
        #%end%------------------------------------%end%#