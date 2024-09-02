import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.stateManager import StateManager

class State:
    """
    Base Template for all States
    """
    def __init__(self, screen: pygame.Surface, state_manager: 'StateManager') -> None:
        self.screen = screen
        self.state_manager = state_manager
    
    def draw(self):
        # Handles UI of State
        pass

    def update(self):
        # Handles LOGIC of State
        pass

    def handle_events(self, events):
        # Handles EVENTS related to State
        pass

# ---------------------------------------------------------------------------
class MainMenu(State):
    """
    Main Menu Screen
    """
    def draw(self):
        self.screen.fill((255, 0, 0))
    
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            print("In states")
            if event.key == pygame.K_e:
                print("Pressed E")
                self.state_manager.change_state("online_menu")
    

class OnlineMenu(State):
    """
    Screen Showed after clicking 'Play Online'
    """
    def draw(self):
        self.screen.fill((0, 255, 0))

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Pressed Q")
                self.state_manager.change_state("main_menu")

class OfflineMenu(State):
    """
    Screen Showed after clicking 'Play Offline'
    """
    pass

class StatsMenu(State):
    """
    Screen that displays Player Stats
    """
    pass

class JoinMenu(State):
    """
    Screen shown after clicking 'Join a Friend' in 'Online Play'
    """
    pass

class HostMenu(State):
    """
    Screen shown after clicking 'Host a Game' in 'Online Play'
    """
    pass

class GameMenu(State):
    """
    The Screen where the game is played
    """
    pass

class GameOverMenu(State):
    """
    Screen shown after the Game Ends
    """
    pass