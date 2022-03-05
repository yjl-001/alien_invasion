import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船并获取图形外接矩阵
        self.image_path = self.ai_settings.get_ship_image_path()
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.scree_rect = self.screen.get_rect()
        # 将每艘新飞船放到屏幕底部中央
        self.rect.centerx = self.scree_rect.centerx
        self.rect.centery = self.scree_rect.centery
        self.rect.bottom = self.scree_rect.bottom
        # 存储小数值
        self.center_x = (float)(self.rect.centerx)
        self.center_y = (float)(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.scree_rect.right:
            self.center_x += self.ai_settings.get_ship_speed()
        elif self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.get_ship_speed()
        elif self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.get_ship_speed()
        elif self.moving_down and self.rect.bottom < self.scree_rect.bottom:
            self.center_y += self.ai_settings.get_ship_speed()

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上底端居中"""
        self.center_x = self.scree_rect.centerx
        self.center_y = self.scree_rect.bottom - (self.rect.height / 2)
