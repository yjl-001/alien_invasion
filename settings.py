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
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 1
        self.bullet_allowed = 3
        # 外星人设置
        self.alien_image_path = "image/alien.bmp"
        self.alien_speed = 0.5
        self.alien_points = 50
        self.fleet_drop_speed = 20
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
        # 加快游戏节奏的设置
        self.speedup_scale = 1.1
        # 提高外星人点数的设置
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.5
        self.bullet_speed = 1
        self.alien_speed = 0.5
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)

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

    def get_alien_speed(self):
        return self.alien_speed

    def get_fleet_drop_speed(self):
        return self.fleet_drop_speed

    def get_bullet_speed(self):
        return self.bullet_speed

    def get_bullet_allowed(self):
        return self.bullet_allowed

    def get_fleet_direction(self):
        return self.fleet_direction

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

    def set_alien_speed(self, alien_speed):
        self.alien_speed = alien_speed

    def set_fleet_drop_speed(self, fleet_drop_speed):
        self.fleet_drop_speed = fleet_drop_speed

    def set_bullet_width(self, bullet_width):
        self.bullet_width = bullet_width

    def set_fleet_direction(self, fleet_direction):
        self.fleet_direction = fleet_direction

    def set_bullet_height(self, bullet_height):
        self.bullet_height = bullet_height

    def set_bullet_allowed(self, bullet_allowed):
        self.bullet_allowed = bullet_allowed
