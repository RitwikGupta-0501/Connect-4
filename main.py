import pygame
import sys


# Game Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 720


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Connect 4")

    # Main Game Loop
    def run(self) -> None:
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            self.screen.fill('blue')
            pygame.display.update()
        
        pygame.quit()
        sys.exit()


class StateManager:
    
# Main Call
if __name__ == '__main__':
    game = Game()
    game.run()
        