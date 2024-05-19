import pygame

tamanho = 1366, 768

superficie = pygame.display.set_mode(tamanho)

pygame.display.set_caption('hehe buai')

fundo = pygame.transform.scale(pygame.image.load('lve/images/fundo.png'), tamanho)


while True:
    # Espaço do display
    superficie.blit(fundo, (0, 0))
    pygame.display.update()