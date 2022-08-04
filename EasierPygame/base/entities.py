from .base import Entity
import pygame

from pygame.constants import *

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