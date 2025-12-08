import pygame
import time
import random
from starting import player, spike



pygame.init()
#Progress counter 
counter = 0
#Best score
best_score = 0
#Character inits
player_width = 55
player_height = 55

#Base colors, can be updated
red = (255, 0, 0)
green = (0, 255, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0, 0, 255)
yella = (255, 255, 0)
see_thru_blue = (0, 0, 255)
black = (0, 0, 0)
#Screen inits
screen_width = 1200
screen_height = 1000

screen_window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
def text_objects(text, font):
    textSurface = font.render(text, True, yella)
    return textSurface, textSurface.get_rect()

#stole buttons from racey
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen_window, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen_window, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("krungthep",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen_window.blit(textSurf, textRect)
#Starting Screen
pygame.font.get_fonts()

def geo_intro():

    block_animation = [background_blocks_right() for x in range(50)]
   
    geo_intro = True
    
    while True:
        #in event of quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        #paint screen prior to moving blocks
        screen_window.fill(see_thru_blue)

        for block in block_animation:
            block.moving_speed()
            block.draw_screen(screen_window)
        
        title_txt = pygame.font.SysFont('krungthep', 60)
        title_screen = title_txt.render('Geometry Dash!', True, (255, 255, 255))
        title_rect = title_screen.get_rect(center = (screen_width // 2, screen_height // 2 - 75))
        screen_window.blit(title_screen, title_rect)
        button("GO!",440,500,125,50,green,bright_green,gameplay)
        button("Quit",630,500,125,50,red,bright_red,gameexit)
        clock.tick(100)

        pygame.display.update()

## Losing screen
def geo_loss(final_score):

    global best_score
    if final_score > best_score:
        best_score = final_score

    block_animation = [background_blocks_right() for x in range(50)]
   
    geo_loss = True
    
    while True:
        #in event of quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        #paint screen prior to moving blocks
        screen_window.fill(see_thru_blue)

        for block in block_animation:
            block.moving_speed()
            block.draw_screen(screen_window)
        
        title_txt = pygame.font.SysFont('krungthep', 60)
        title_screen = title_txt.render('You Lost!', True, (255, 255, 255))
        title_rect = title_screen.get_rect(center = (screen_width // 2, screen_height // 2 - 75))
        screen_window.blit(title_screen, title_rect)

        score_font = pygame.font.SysFont('krungthep', 40)
        score_text = score_font.render(f"Score: {final_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center = (screen_width // 2, screen_height // 2 - 150))
        screen_window.blit(score_text, score_rect)

        best_text = score_font.render(f"Best: {best_score}", True, (255, 255, 255))
        best_rect = best_text.get_rect(topleft = (20, 80))
        screen_window.blit(best_text, best_rect)

        button("Try Again!",440,500,125,50,green,bright_green,gameplay)
        button("Quit",630,500,125,50,red,bright_red,gameexit)
        clock.tick(60)

        pygame.display.update()

class background_blocks_right():
    def __init__(self):
        self.h = random.randint(25, 65)
        self.w = self.h
        self.s = random.randint(10, 15)
        self.x = random.randint(-300, 1200)
        self.y = random.randint(0, 1000)
        self.c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def moving_speed(self):
        self.x += self.s 
        if self.x >= 1200 + self.w:
            self.__init__()

    def draw_screen(self, screen_window):
        pygame.draw.rect(screen_window, self.c, (self.x, self.y, self.w, self.h))
def gameexit():
    pygame.quit()
    quit()

class buildingblocks():
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
  #drawing blocks
  def draw_block(self, top):
    pygame.draw.rect(top, yella, (self.x, self.y, self.w, self.h))

def gameplay():
    player_x_val = screen_width * .05
    player_y_val = screen_height * .1
    ground_hei = int(screen_height * .75)

    player_cube = player(height =55, width = 55, x = int(screen_width * .05), y = ground_hei)

    spikes = spike(height = random.randint(40, 60), width = random.randint(40, 60), x = screen_width + 1, y = ground_hei)
    spikes_ex = spike(height = 65, width = 45, x = 1500, y = 750)
    spikes_ex2 = spike(height = 175, width = 45, x = 1700, y = 650)
    spikes_ex3 = spike(height = 265, width = 45, x = 1900, y = 550)
    spikes_s = random.randint(10, 20)

    #dimensions of jumpable surfaves
    #x y w h
    towers = [buildingblocks(1500, 745, 45, 60), buildingblocks(1700, 645, 45, 160), buildingblocks(1900, 545, 45, 260) ]
    

    score = 0
    score_font = pygame.font.SysFont('krungthep', 30)
    start_time = pygame.time.get_ticks()

#im not gna lie this might not work youtube is teaching me how to do ts pygame stuff


    gameexit = False

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_cube.jump_ability()
                if event.key == pygame.K_ESCAPE:
                    return
        player_cube.movement(ground_hei)
        #this might ruin the code ngl
        ontower = False 
        playablock = pygame.Rect(player_cube.x, player_cube.y, player_cube.width, player_cube.height)
        for x in towers:
            tower_struc = pygame.Rect(x.x,x.y,x.w,x.h)
            if player_cube.velocity_y>= 0 and playablock.colliderect(tower_struc):
                player_cube.y = x.y - player_cube.height 
                player_cube.velocity_y = 0
                player_cube.ground = True
                ontower = True
                

        spikes.spikes_move(spikes_s)
        spikes_ex.spikes_move(10)
        spikes_ex2.spikes_move(10)
        spikes_ex3.spikes_move(10)
        spikes.spike_create(screen_width, ground_hei)
        for x in towers:
            x.x -= 10

        elapsed_ms = pygame.time.get_ticks() - start_time
        score = elapsed_ms // 100 

        if spikes.collision(player_cube):
            geo_loss(score)
            return
        if spikes_ex.collision(player_cube):
            geo_loss(score)
            return
        if spikes_ex2.collision(player_cube):
            geo_loss(score)
            return
        if spikes_ex3.collision(player_cube):
            geo_loss(score)
            return

        screen_window.fill(see_thru_blue)
        #floor
        pygame.draw.line(screen_window, red, (0, ground_hei + player_cube.height),(screen_width,ground_hei + player_cube.height), 1)
        pygame.draw.rect(screen_window, yella, (player_cube.x, player_cube.y, player_cube.width, player_cube.height))
        #spike
        pygame.draw.rect(screen_window, red, (spikes.x, spikes.y, spikes.width, spikes.height))
        pygame.draw.rect(screen_window, see_thru_blue, (spikes_ex.x, spikes_ex.y, spikes_ex.width, spikes_ex.height))
        pygame.draw.rect(screen_window, see_thru_blue, (spikes_ex2.x, spikes_ex2.y, spikes_ex2.width, spikes_ex2.height))
        pygame.draw.rect(screen_window, see_thru_blue, (spikes_ex3.x, spikes_ex3.y, spikes_ex3.width, spikes_ex3.height))
        score_text_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen_window.blit(score_text_surface, (20, 20))

        best_text_surface = score_font.render(f"Best: {best_score}", True, (255, 255, 255))
        best_rect = best_text_surface.get_rect(topright=(screen_width - 20, 20))
        screen_window.blit(best_text_surface, best_rect)

        for x in towers:
            x.draw_block(screen_window)
        clock.tick(60)
        pygame.display.update() 
        
#im not gna lie this might not work youtube is teaching me how to do ts pygame stuff^^

##Progress counter


geo_intro()