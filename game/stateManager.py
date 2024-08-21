from . import states

class StateManagerError(Exception):
    """
    Raised when the StateManager encounters errors
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return {self.message}

# -----------------------------------------------------------------------------------------

class StateManager:
    """
    A class that centrally manages all Game States.
    """

    def __init__(self, screen) -> None:
        self.screen = screen
        self.states = {}
        self.current_state = None
        self.initialize_states()
    
    def initialize_states(self) -> None:
        self.states['main_menu'] = states.MainMenu(self.screen, self)
        self.states['online_menu'] = states.OnlineMenu(self.screen, self)
        self.states['offline_menu'] = states.OfflineMenu(self.screen, self)
        self.states['stats_menu'] = states.StatsMenu(self.screen, self)
        self.states['join_menu'] = states.JoinMenu(self.screen, self)
        self.states['host_menu'] = states.HostMenu(self.screen, self)
        self.states['game_menu'] = states.GameMenu(self.screen, self)
        self.states['gameover_menu'] = states.GameOverMenu(self.screen, self)
    
    def change_state(self, new_state:states.State) -> None:
        if new_state in self.states:
            self.current_state = self.states[new_state]
        else:
            raise StateManagerError(f"State '{new_state}' not found.")
    
    def update(self)  -> None:
        if self.current_state:
            self.current_state.update()
        else:
            raise StateManagerError("Current State is NONE.")
        
    def draw(self) -> None:
        if self.change_state:
            self.current_state.draw()
        else:
            raise StateManagerError("Current State is NONE.")
    
    def handle_events(self, events) -> None:
        if self.change_state:
            self.current_state.handle_events()
        else:
            raise StateManagerError("Current State is NONE.")