import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # 在(0, 0)处创建子弹，再移动到正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.get_bullet_width(), ai_settings.get_bullet_height())
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        # 存储用小数表示的子弹位置
        self.position_y = (float)(self.rect.y)
        self.color = ai_settings.get_bullet_color()
        self.speed = ai_settings.get_bullet_speed()

    def update(self):
        self.position_y -= self.speed
        self.rect.y = self.position_y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
