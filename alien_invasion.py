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

  #start the main loop for the game
  while True:
    #checks for mouse and keyboard events
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    bullets.update()
    #updates the screen
    gf.update_screen(ai_settings, screen, ship, bullets)

run_game()