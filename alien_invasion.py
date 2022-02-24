import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    # cria uma espaçonave
    ship = Ship(screen)

    # Define a cor de fundo
    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo

    while True:
        # observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # deixa a tela mais recente visível
        pygame.display.flip()

run_game()