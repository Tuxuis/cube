import sys
import pygame
from pygame.locals import *


class colors:
    white = (255, 255, 255)
    blue = (0, 0, 255)

def exit_check():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def main():
    pygame.init()
    display = pygame.display.set_mode((500, 400), 0, 32)

    x = 100
    y = 100

    while True:
        key = pygame.key.get_pressed()
        exit_check()

        display.fill(colors.white)
        pygame.draw.rect(display, colors.blue, (x, y, 50, 50))

        if key[K_d]:
            x = x + 7
        if key[K_a]:
            x = x - 7
        if key[K_w]:
            y = y - 7
        if key[K_s]:
            y = y + 7

        if x - 140 > display.get_width():
            x = - 0.5
        if x <- 140:
            x = + 450

        if y - 70 > display.get_width():
            y = - 0.5 
        if y <- 70:
            y = + 550
        


        pygame.display.update()
        pygame.time.delay(10)

if __name__ == "__main__":
    main()
