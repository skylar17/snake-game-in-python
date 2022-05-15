from contextlib import redirect_stderr
import pygame 
from pygame.locals import * 

import time
import random



pygame.init()

#set up the output screen
screen_width = w = 800
screen_height = h = 600
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption('Snake Game by Shivani')

# my_font = pygame.font.SysFont('Times New Roman', 25, bold=True)
#--------------------------------------------
# Initialing Color
RED = (255,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)

#------------------
screen.fill(WHITE)
#------------------------------------------
#to keep the screen open 
def hold():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        pygame.display.flip()
hold()
#---------------------------------------------------------

# Initializing playing surface
# play_surface = pygame.display.set_mode((screen_width,screen_height-50))


# Drawing Rectangle
rect = rect(300, 300, 300, 300)
play_surface = pygame.draw.rect(screen, RED, rect,  2)
hold()

# bg_img = pygame.image.load("C:/Users/shiva/OneDrive/shiva-pc/github-repos-onedrive/snake-game-in-python/images/bg-1.jpygame")
# play_surface.blit(pygame.transform.scale(bg_img, (0, screen_height-50), play_surface))




  

# -==========================================================




# #score board
# def scoreinfo(score):
#     score_dis = my_font.render("Your Score: " + str(score), True)
#     screen.blit(score_dis, [0, 0])
#-------------------------------------------------


# rect(surface, color, rect, width=2, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)



