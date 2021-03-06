import pygame

from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    # cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Define a cor de fundo
    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo

    while True:
        # observa eventos de teclado e de mouse
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
