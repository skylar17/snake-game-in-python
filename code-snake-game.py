import pygame as pg
import time
import random
 
pg.init()

#set up the output screen
screen_width=500
screen_height=500
screen = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption('Snake Game by Shivani')
#to keep the screen open 
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run =False


pic = pg.image.load("Resources/bg-1.jpg")
screen.blit(pg.transform.scale(pic, (500, 500)), (0, 0))
pg.display.flip()
while True:
    pg.event.pump()
    event = pg.event.wait()
    if event.type == QUIT:
        pg.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pg.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pg.transform.scale(pic, event.dict['size']), (0, 0))
        pg.display.flip()







# bg_image = pg.image.load("Resources/bg-1.jpg")
# # screen.blit(pg.transform.scale(bg_image, (800, 600)))
# bg_image = pg.transform.scale(bg_image, (800, 600))
# rect = bg_image.get_rect()
# rect = rect.move((800, 600))
# screen.blit(bg_image, rect)






# # clock = pg.time.Clock()




# pg.quit()