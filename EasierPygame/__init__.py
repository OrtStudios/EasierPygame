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

from .sounds import Sounds
from .cutsences import Cutscence

class MainWindow:
    def __init__(
        self,
        width: int,
        height: int,
        title: str,
        resizable: bool,
        iconPath: str = None,
        backgroundColor: tuple = (0, 0, 0),
    ) -> None:
        """Create a window for the game.

        Args:
            width (int): the width of the window.
            height (int): the height of the window.
            title (str): the title of the window.
            resizable (bool): whether the window is resizable.

        Returns:
            pygame.surface.Surface: the window.
        """  
        self.window = pygame.display.set_mode(
            (
                width,
                height
            ), 
            pygame.RESIZABLE if resizable else None
        )

        self.startingScreenWidth = width
        self.startingScreenHeight = height

        self.backgroundColor = backgroundColor

        # title
        pygame.display.set_caption(title)

        # icon
        if iconPath is not None:
            self.icon = pygame.image.load(iconPath)
            pygame.display.set_icon(self.icon)
    
    def NewFrame(self) -> None:
        """New frame.
        """
        self.window.fill(self.backgroundColor)

    def GetScreen(self) -> pygame.surface.Surface:
        """Get the screen.

        Returns:
            pygame.surface.Surface: the screen.
        """
        return self.window

    def GetScreenWidth(self) -> int:
        """Get the width of the screen.

        Returns:
            int: the width of the screen.
        """
        return self.window.get_width()

    def GetScreenHeight(self) -> int:
        """Get the height of the screen.

        Returns:
            int: the height of the screen.
        """
        return self.window.get_height()
    
    def GetStartingScreenWidth(self) -> int:
        """Get the starting width of the screen.

        Returns:
            int: the starting width of the screen.
        """
        return self.startingScreenWidth
    
    def GetStartingScreenHeight(self) -> int:
        """Get the starting height of the screen.

        Returns:
            int: the starting height of the screen.
        """
        return self.startingScreenHeight
    
    def UpdateScreen(self) -> None:
        """Update the screen.
        """
        for event in pygame.event.get():
            if event.type == QUIT: #if you closing the window 
                quit()

        pygame.display.update()

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

#--------------------------------------------< Buttons >--------------------------------------------#
class Button(Entity):
    def __init__(
        self,
        screen: pygame.Surface,

        x: int,
        y: int,

        starting_screen_width: int,
        width: int,

        starting_screen_height: int,
        height: int,

        texture_path: str,
        hover_texture_path: str,
        completed_texture_path: str = None,
        locked_texture_path: str = None,

        unlocked: bool = True,
        completed: bool = False
    ):
        
        super().__init__(
            screen,
            x,
            y,
            starting_screen_width,
            width,
            starting_screen_height,
            height,
            texture_path
        )

        self.hover     = False
        self.clickVar  = False
        self.unlocked  = unlocked
        self.completed = completed

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        
        #Textures
        self.hover_texture = pygame.transform.scale( #change the scale of the given hover image
            pygame.image.load(
                    hover_texture_path
                ),
                (self.rect.width, self.rect.height)
            )
    
        if locked_texture_path is not None:
            self.locked_texture = pygame.transform.scale( #change the scale of the given image
                pygame.image.load(
                    locked_texture_path
                ),
                (self.rect.width, self.rect.height)
            )
        
        if completed_texture_path is not None:
            self.completed_texture = pygame.transform.scale( #change the scale of the given hover image
                pygame.image.load(
                        completed_texture_path
                    ),
                (self.rect.width, self.rect.height)
            )
    
    def update(self):
        """update self and draw him on the screen
        """
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clickVar = True
                else:
                    self.clickVar = False
            
            if event.type == QUIT:
                quit()

        self.mouse_hover() #go to the func hover
        self.draw() #go to the func draw
    
    def draw(self):
        """draw the right texture on the screen
        """        
        if not self.unlocked:
            self.screen.blit(self.locked_texture, (self.x, self.y)) #show the locked texture
    
        elif self.hover: #if the mouse is on the button
            self.screen.blit(self.hover_texture, (self.x, self.y)) #show the hover texture
    
        elif self.completed:
            self.screen.blit(self.completed_texture, (self.x, self.y)) #show the completed texture
    
        else:
            super().draw()
    
    def mouse_hover(self):
        """change the hover var of the entity if the mouse is hover the button
        """        
        if self.rect.collidepoint(self.mouse_x, self.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
    
    def click(self):
        """check if the user clicked on the entity

        Returns:
            bool: is the button clicked
        """
        if self.hover and self.clickVar and self.unlocked: #if click on the button
            self.clickVar = False
            return True
        else:
            return False

#----------------------------------< Clickable Invisible Object >----------------------------------#
class Clickable_Invisible_object(Entity):
    def __init__(
        self,
        screen: pygame.Surface,

        x: float,
        y: float,

        starting_screen_width: int,
        width:  int,
        starting_screen_height: int,
        height: int
        ):

        super().__init__(
            screen,
            x,
            y,
            starting_screen_width,
            width,
            starting_screen_height,
            height
        )

        self.hover = False
        self.click = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
                else:
                    self.click = False

        self.mouse_hover()

    def mouse_hover(self):
        if self.rect.collidepoint(self.mouse_x, self.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
    
    def click(self):
        """check if the user clicked on the entity

        Returns:
            bool: is the button clicked
        """
        if self.hover and self.click: #if click on the button
            self.click = False
            return True
        else:
            return False

#------------------------------------< Clickable Text Object >------------------------------------#
class Clickable_Text_object(Entity):
    def __init__(
        self,
        screen: pygame.Surface,

        x: float,
        y: float,

        starting_screen_width: int,
        width:  int,
        starting_screen_height: int,
        height: int,

        text: str,
        text_color: tuple,
        font_size: int,
        font_path: str
        ):

        super().__init__(
            screen,
            x,
            y,
            starting_screen_width,
            width,
            starting_screen_height,
            height
        )

        #is the mouse hover the rect
        self.hover = False

        #font and text render
        self.font = pygame.font.Font(
            font_path, font_size
        )
        self.text = self.font.render(text, 1, text_color)

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def update(self):
        #blit
        self.screen.blit(self.text, (self.rect.x, self.rect.y))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        #is you clicked the rect
        self.mouse_hover()

    def mouse_hover(self):
        if self.rect.collidepoint(self.mouse_x, self.mouse_y): #if the mouse is on the button
            self.hover = True
        else:
            self.hover = False
    
    def click(self):
        """check if the user clicked on the entity

        Returns:
            bool: is the button clicked
        """
        if self.hover and self.click: #if click on the button
            self.click = False
            return True
        else:
            return False

#--------------------------------------------< Just An Image >--------------------------------------------#
class Just_an_image(Entity):
    def __init__(
        self,
        screen: pygame.Surface,

        x: float,
        y: float,

        starting_screen_width: int,
        width:  int,
        starting_screen_height: int,
        height: int,

        image_path = "file name"
        ):
        
        
        super().__init__(
            screen,
            x,
            y,
            starting_screen_width,
            width,
            starting_screen_height,
            height,
            image_path
        )

    def update(self, x, y):
        #position
        self.x = x
        self.y = y

        #rect
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #show image
        self.draw()
#%end%-----------< The End >-----------%end%#
