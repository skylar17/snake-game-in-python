import pygame as pg
import time
import random
 
pg.init()

#set up the output screen
screen_width=800
screen_height=600
screen = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption('Snake Game by Shivani')

bg_img = pg.image.load("C:/Users/shiva/OneDrive/shiva-pc/github-repos-onedrive/snake-game-in-python/images/bg-1.jpg")
screen.blit(bg_img, (0,0))


#to keep the screen open 
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run =False
    pg.display.flip()
#------------------------------------------



# clock = pg.time.Clock()
# done = False
# while not done:

#     # Handle user-input
#     for event in pg.event.get():
#         if ( event.type == pg.QUIT ):
#             done = True

#     # Update the window, but not more than 60fps
#     screen.blit( bg_img, ( 800,800 ) )
#     pg.display.flip()                    # <-- Flush drawing ops to the screen

#     # Clamp FPS
#     clock.tick_busy_loop( 60 )

# pg.quit()
# # screen.blit(pg.transform.scale(bg_image, (800, 600)))
# #bg_image = pg.transform.scale(bg_image, (800, 600))









# # # clock = pg.time.Clock()




# # pg.quit()