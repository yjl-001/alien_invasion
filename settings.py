class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_image_path = "image/ship.bmp"
        self.ship_speed = 0.5
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 1
        self.bullet_allowed = 3
        # 外星人设置
        self.alien_image_path = "image/alien.bmp"

    def get_screen_width(self):
        return self.screen_width

    def get_bullet_width(self):
        return self.bullet_width

    def get_screen_height(self):
        return self.screen_height

    def get_bullet_height(self):
        return self.bullet_height

    def get_bg_color(self):
        return self.bg_color

    def get_bullet_color(self):
        return self.bullet_color

    def get_ship_image_path(self):
        return self.ship_image_path

    def get_alien_image_path(self):
        return self.alien_image_path

    def get_ship_speed(self):
        return self.ship_speed

    def get_bullet_speed(self):
        return self.bullet_speed

    def get_bullet_allowed(self):
        return self.bullet_allowed

    def set_bg_color(self, x, y, z):
        self.bg_color = (x, y, z)

    def set_bullet_color(self, x, y, z):
        self.bullet_color = (x, y, z)

    def set_ship_image_path(self, ship_image_path):
        self.ship_image_path = ship_image_path

    def set_alien_image_path(self, alien_image_path):
        self.alien_image_path = alien_image_path

    def set_ship_speed(self, ship_speed):
        self.ship_speed = ship_speed

    def set_bullet_speed(self, bullet_speed):
        self.bullet_speed = bullet_speed

    def set_bullet_width(self, bullet_width):
        self.bullet_width = bullet_width

    def set_bullet_height(self, bullet_height):
        self.bullet_height = bullet_height

    def set_bullet_allowed(self, bullet_allowed):
        self.bullet_allowed = bullet_allowed
