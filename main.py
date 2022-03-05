from game_functions import *
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_states import GameStates


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.get_screen_width(), ai_settings.get_screen_height()))
    screen.fill(ai_settings.get_bg_color())
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于统计游戏信息的实例
    stats = GameStates(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 更新飞船、子弹和外星人的位置
            ship.update()
            update_bullets(bullets, ai_settings, screen, ship, aliens)
            update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # 显示屏幕
            update_screen(ai_settings, screen, ship, bullets, aliens)


# 程序入口
if __name__ == '__main__':
    run_game()
