import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 飞船移动事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """处理按键按下的事件"""
    # 控制飞船上下左右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 开火
    elif event.key == pygame.K_f:
        fire_bullet(ai_settings, screen, ship, bullets)
    # 退出游戏快捷键
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """处理按键松开的事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕"""
    screen.fill(ai_settings.get_bg_color())
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(bullets, ai_settings, screen, ship, aliens):
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 子弹与外星人进行碰撞检测
    check_bullets_aliens_collsions(ai_settings, screen, ship, aliens, bullets)


def check_bullets_aliens_collsions(ai_settings, screen, ship, aliens, bullets):
    """子弹与外星人进行碰撞检测"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有子弹并创建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # 更新外星人位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # 检测外星人是否到达底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应飞船被外星人撞到"""
    # 将ship_left减一
    stats.ships_left -= 1
    if stats.ships_left > 0:
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并把飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到子弹数量的限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.get_bullet_allowed():
        # 创建新子弹，并添加到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 设置外星人的间距
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建一群外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行外星人的个数"""
    available_space_x = ai_settings.get_screen_width() - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算外星人的行数"""
    available_space_y = (ai_settings.get_screen_height() - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建外星人并设置位置"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.position_x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.position_x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 添加外星人到编组中
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取响应"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整个外星人群下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.get_fleet_drop_speed()
    ai_settings.fleet_direction *= -1
