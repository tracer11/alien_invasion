class Settings():

  def __init__(self):
    #screen settings
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 230)
    #ship settings
    self.ship_speed_factor = 5
    #bullet settings
    self.bullet_speed_factor = 5
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60, 60, 60
    self.bullets_allowed = 10
    #alien settings
    self.alien_speed_factor = 1
    self.fleet_drop_speed = 10
    self.fleet_direction = 1

