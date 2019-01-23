import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船、一个子弹编组、一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环
    while True:
        #响应按键和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



if __name__ == "__main__":
    run_game()