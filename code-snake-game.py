
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
#--------------------------------------------
# # Defining Colors
WHITE=(255,255,255)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
#---------------------------------------------------------
screen.fill(WHITE)
bg_img = pygame.image.load("C:/Users/shiva/OneDrive/shiva-pc/github-repos-onedrive/snake-game-in-python/images/bg-1.jpg")
screen.blit(pygame.transform.scale(bg_img, (w,h-35)), (0,0))

clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Times New Roman', 20, bold=True)
def scoreinfo(score):
    score_display = my_font.render("Your Score is: " + str(score), True, (0,0,0), BLUE)
    screen.blit(score_display, [0, 579])






#to keep the screen open 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
#============================bg works until here=============================================

#------------------------------------------


# Initializing playing surface
# play_surface = pygame.display.set_mode((w,h-50))



# # Drawing Rectangle
# rect = Rect( 750, 600, 750, 600)
# play_surface = pygame.draw.rect(screen, RED, rect,  2)

# # bg_img = pygame.image.load("C:/Users/shiva/OneDrive/shiva-pc/github-repos-onedrive/snake-game-in-python/images/bg-1.jpg")
# # play_surface.blit(bg_img, (0,0))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEMOTION:
#             running = False
#     pygame.display.flip()









  

# -==========================================================




# #score board
# def scoreinfo(score):
#     score_dis = my_font.render("Your Score: " + str(score), True)
#     screen.blit(score_dis, [0, 0])
#-------------------------------------------------


# rect(surface, color, rect, width=2, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)


pygame.quit()
