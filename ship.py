import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimar para o centro da espaçonave
        self.center = float(self.rect.centerx)

        # flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        # Atualiza o objeto rect de acordo com self.center
        self.rect_centerx = self.center

    def blitme(self):
        """desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
