import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  #initialize game and create screen object
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  ship = Ship(ai_settings, screen)
  bullets = Group()
  aliens = Group()

  gf.create_fleet(ai_settings, screen, ship, aliens)

  #start the main loop for the game
  while True:
    #checks for mouse and keyboard events
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
    gf.update_aliens(ai_settings, aliens)
    #updates the screen
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()