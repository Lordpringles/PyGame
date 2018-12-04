import pygame
import time
import random

pygame.init()

sWidth = 800
sHeight = 600
display = (sWidth, sHeight)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
lightblue = (0, 255, 255)

gameDisplay = pygame.display.set_mode(display)
pygame.display.set_caption('PyGame with Snowden the Second')
clock = pygame.time.Clock()

carImg = pygame.image.load('Car_Purple_Front.png')
carImg = pygame.transform.scale(carImg, (50, 80))

def things(thingx, thingy, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, (thingx, thingy, thingW, thingH))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurf = font.render(text, True, black)
    return textSurf, textSurf.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((sWidth / 2, sHeight /2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

    time.sleep(2.5)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():

    x = (sWidth * 0.45)
    y = (sHeight * 0.8)

    thing_startx = random.randrange(250, 450)
    thing_starty = -500
    thing_speed = 4
    thing_width = 50
    thing_height = 100

    gameExit = False
    while not (gameExit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= 5
        if keys[pygame.K_d]:
            x += 5

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, purple)
        thing_starty += thing_speed

        car(x,y)

        if x > sWidth - 50 or x < 0:
            crash()

        if thing_starty > sHeight:
            thing_starty = 0 - thing_height
            thing_startx = random.randint(250, 450)


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
