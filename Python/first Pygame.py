import pygame
import os
from pygame.locals import *


pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')


current_path = os.path.dirname(__file__)  # where .py file is located
# the resource folder path
resource_path = os.path.join(current_path, 'resources')
image_path = os.path.join(resource_path, 'images')  # the image folder path

black = (0, 0, 0)
white = (255, 255, 255)


clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load(os.path.join(image_path, 'racecar.png'))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x = (display_width * 0.45)
y = (display_width * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
