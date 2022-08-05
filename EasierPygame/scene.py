import pygame

from EasierPygame.application import Application

class SceneType:
    """Scene type.
    """

class Menu(SceneType):
    """Menu.
    """

class MainMenu(Menu):
    """Main menu.
    """

class Settings(Menu):
    """Settings.
    """

class CustomMenu(Menu):
    """Custom menu.
    """

class Other(SceneType):
    """Custom.
    """

class Scene:
    """this class is used to create a scene.
    a scene is a part of the application also can be described like a view or a page.
    the scene covers the hole screen and used to display the content.
    it's the base of the application.
    you can create a scene by using the Scene class.
    you can also use more then one scene in the application and you can switch between them.
    """    
    def __init__(
        self,
        name: str,
        id: int,
        screen: Application,
        sceneType: SceneType,
        backgroundColor: tuple,
    ) -> None:
        
        self.name = name
        self.id = id

        self.screen = screen
        self.sceneType = sceneType

        self.backgroundColor = backgroundColor

        #{
        #    "name": {
        #        "path": "",
        #        "object": None,
        #        "pos": (0, 0),
        #        "size": (0, 0)
        #    }
        #}
        self.images = {}
    
    def SetBackgroundImage(self, path: str):
        size = (self.screen.GetScreenWidth(), self.screen.GetScreenHeight())

        self.images["background"] = {
            "path": path,
            "object": pygame.transform.scale(
                pygame.image.load(
                    path
                ),
                size
            ),
            "pos": (0, 0),
            "size": size
        }

    def SetBackgroundColor(self, color: tuple):
        self.backgroundColor = color

    def Update(self):
        self.screen.window.fill(self.backgroundColor)

        for key, value in self.images:
            self.screen.blit(
                self.images[key]["object"],
                self.images[key]["pos"]
            )