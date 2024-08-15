import pygame

class State:
    pass

# ---------------------------------------------------------------------------
class MainMenu(State):
    """
    Main Menu Screen
    """
    pass

class OnlineMenu(State):
    """
    Screen Showed after clicking 'Play Online'
    """
    pass

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