import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load(ai_settings.get_alien_image_path())
        self.rect = self.image.get_rect()
        # 每个外星人最初都位于左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的正确位置
        self.position_x = (float)(self.rect.x)
        self.position_y = (float)(self.rect.y)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.position_x += self.ai_settings.get_alien_speed() * self.ai_settings.get_fleet_direction()
        self.rect.x = self.position_x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
