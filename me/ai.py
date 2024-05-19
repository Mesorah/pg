import pygame
import sys

from settings import Settings

class Ai:
    def __init__(self,):
        pygame.init()
        self.clock = pygame.time.Clock() # frames
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('jogo lsa')

        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color) # preenche a tela

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = Ai()
    ai.run_game()