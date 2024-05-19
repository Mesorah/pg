import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Classe geral para gerenciar ativos e comportamento do jogo """

    def __init__(self):
        """ Inicializa o jogo e crie recursos do jogo """

        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))


        pygame.display.set_caption('Alien invasion')

        self.ship = Ship(self)

        # Define a cor do background
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """ Inicia o loop principal do jogo """

        while True:

            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
        
            self.ship.blitme()

            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
