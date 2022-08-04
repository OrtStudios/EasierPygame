import pygame

from .base import quit

class Application:
    def __init__(
        self,
        width: int,
        height: int,
        title: str,
        resizable: bool,
        iconPath: str = None,
        backgroundColor: tuple = (0, 0, 0)
    ) -> None:
        """Create the application.

        Args:
            width (int): the width of the application.
            height (int): the height of the application.
            title (str): the title of the application.
            resizable (bool): whether the application is resizable.
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
            if event.type == pygame.QUIT: #if you closing the window 
                quit()

        pygame.display.update()