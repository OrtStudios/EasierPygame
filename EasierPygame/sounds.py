import pygame, os
from pygame.locals import *

class Sounds:

    volume = 0
    sounds_dict = {}

    @staticmethod
    def change_volume(volume: float):
        #%start%------------------------------------%start%#
        """
        change the volume of the music and sound effects
        
        Return:
            float: the new volume
        """

        if 0 <= volume <= 1:
            Sounds.volume = volume
        else:
            if volume < 0:
                Sounds.volume = 0
            else:
                Sounds.volume = 1

        for key in Sounds.sounds_dict:
            pygame.mixer.Sound.set_volume(Sounds.sounds_dict[key], Sounds.volume)

        return Sounds.volume
        #%end%------------------------------------%end%#

    @staticmethod
    def load_sounds(path: str, key: str) -> None:
        #%start%------------------------------------%start%#
        """ load sounds and sfx to the dict (pygame.mixer.Sound)

        Args:
            path (str): the path of the sound file(including extension).
            key (str): the key in the dict.
        """              
        # ?----------------------------------------load sound----------------------------------------?#
        if os.path.exists(path):
            Sounds.sounds_dict[key] = pygame.mixer.Sound(path)

        # ?----------------------------------------set volume----------------------------------------?#
        pygame.mixer.Sound.set_volume(Sounds.sounds_dict[key], Sounds.volume)
        #%end%------------------------------------%end%#

    #%end%-----------------------------------------------------------------------%end%#
