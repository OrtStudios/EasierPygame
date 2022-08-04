import pygame

class Entity:
    def __init__(
        self,
        screen: pygame.Surface,

        x: float,
        y: float,

        starting_screen_width: int,
        width: int,

        starting_screen_height: int,
        height: int,

        texture_path = "blank.png"
    ):
        self.screen = screen
        self.x = x
        self.y = y

        self.width = Resize.resizeWidth(
            starting_screen_width,
            width,
            screen.get_width()
        )
        self.height = Resize.resizeHeight(
            starting_screen_height,
            height,
            screen.get_height()
        )
        
        self.rect = pygame.Rect(
            x,
            y,
            self.width,
            self.height
        )

        self.starting_screen_width  = screen.get_width()
        self.starting_screen_height = screen.get_height()
        self.starting_width         = width
        self.starting_height        = height

        self.texture = pygame.transform.scale(
            pygame.image.load(
                    texture_path
                ),
            (self.rect.width, self.rect.height)
        )
    
    def update(self):
        self.draw()
    
    def draw(self):
        self.screen.blit(
            self.texture,
            (self.x, self.y)
        )

class Resize:

    @staticmethod
    def resizeWidth(starting_screen_width, size_for_the_starting_screen_width, screen_width):
        #%start%------------------------------------%start%#
        """
        you can resize the width of your objects with the original screen width and the width of the object in that screen width
        -> returns float <-
        """
        x = starting_screen_width / size_for_the_starting_screen_width
        return float(screen_width / x)
        #%end%------------------------------------%end%#
    
    @staticmethod
    def resizeHeight(starting_screen_height, size_for_the_starting_screen_height, screen_height):
        #%start%------------------------------------%start%#
        """
        you can resize the height of your objects with the original screen height and the height of the object in that screen height
        -> returns float <-
        """
        y = starting_screen_height / size_for_the_starting_screen_height
        return float(screen_height / y)
        #%end%------------------------------------%end%#

    @staticmethod
    def Resize(
        screen,
        original_screen_width = 900,
        original_screen_height = 500,
        size_for_the_original_screen_width = 10,
        size_for_the_original_screen_height = 10
        ):
        #%start%------------------------------------%start%#
        """
        you can resize your objects with the original screen size and the size of this object for the original  screen size
        -> return a tuple of the width and hight of the object in the current screen resolution <-
        """
        width = Resize.resizeWidth(
            original_screen_width, size_for_the_original_screen_width, screen.get_width()
            )
        hight = Resize.resizeHeight(
            original_screen_height, size_for_the_original_screen_height, screen.get_height()
            )
        return (width, hight)
        #%end%------------------------------------%end%#
    
    @staticmethod
    def ChangePos(
            obj: Entity,
            screen_width: int,
            screen_height: int,
            width_before: int,
            height_before: int
        ):
        #%start%------------------------------------%start%#
        """
        for none static objects only!
        change the pos of the object based on the resizing of the screen
        -> return object <-
        """
        if (screen_width != width_before) or (screen_height != height_before):
            obj_x = obj.x
            obj_y = obj.y
            screen_w: int = screen_width
            screen_h: int = screen_height
            first_set_px = obj_x / width_before
            first_set_py = obj_y / height_before
            obj.x = first_set_px * screen_w
            obj.y = first_set_py * screen_h
            width_before = screen_w
            height_before = screen_h
            return obj, width_before, height_before
        #%end%------------------------------------%end%#
    
    #%end%-----------------------------------------------------------------------%end%#