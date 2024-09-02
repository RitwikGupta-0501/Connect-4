import pygame
import sys
from game.stateManager import StateManager

# Game Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 720


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.state_manager = StateManager(self.screen)
        self.state_manager.change_state('main_menu')
        pygame.display.set_caption("Connect 4")

    # Main Game Loop
    def run(self) -> None:
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    self.state_manager.handle_events(event)
            
            self.state_manager.draw()
            self.state_manager.update()

            pygame.display.update() 
        pygame.quit()
        sys.exit()
    
# Main Call
if __name__ == '__main__':
    game = Game()
    game.run()
        