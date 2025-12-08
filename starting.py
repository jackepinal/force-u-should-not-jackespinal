import random
import pygame 

class obstacle_objects():
  def __init__(self, height, width, x, y):
    self.height = height
    self.width = width
    self.x = x
    self.y = y

class player(obstacle_objects):
  def __init__(self, height, width, x, y):
    super().__init__(height, width, x, y)
    self.velocity_x = 0
    self.velocity_y = 0
    self.jump_y = 15
    self.grav = 1
    self.life = True
    self.ground = True

  def movement(self, ground_y_val):
    #for vert movement etc
    self.velocity_y += self.grav
  
    self.y += self.velocity_y
#for on ground
    if self.y >= ground_y_val:
      self.y = ground_y_val
      self.velocity_y = 0
      self.ground = True


  def jump_ability(self):
    #can only jump if on ground
    if self.ground:
      self.velocity_y -= self.jump_y

      self.ground = False

class spike(obstacle_objects):
  def __init__(self, height, width, x, y):
    super().__init__(height, width, x, y)
  
  def spikes_move(self, speed):
    self.x -= speed
  
  def spike_create(self, screen_width, ground_hei):
    if self.x + screen_width < 0:
      self.x = screen_width + 1
      self.y = ground_hei
  
  def collision(self, player):
    playerrect = pygame.Rect(player.x, player.y, player.width, player.height)
    spikerect = pygame.Rect(self.x, self.y, self.width, self.height)
    return spikerect.colliderect(playerrect)
  
  
  # blocks for character to jump onto and over

class buildingblocks():
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  #drawing blocks
  def draw_block(self, surface):
    pygame.draw.rect(surface, see_thru_blue(self.x, self.y, self.w, self.h))