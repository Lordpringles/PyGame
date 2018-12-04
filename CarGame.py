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
orange = (0, 255, 255)
vel = 5
car_width = 50
car_height = 80
car2_width = 50
car2_height = 80

gameDisplay = pygame.display.set_mode(display)
pygame.display.set_caption('My Own Atari-like Car Game')
clock = pygame.time.Clock()

carImg = pygame.image.load('Car_Purple_Front.png')
carImg = pygame.transform.scale(carImg, (50, 80))
carImg2 = pygame.image.load('Car_Green_Front.png')
carImg2 = pygame.transform.scale(carImg2, (50, 80))
grassWidth = 300
grassHeight = 600
stripeWidth = 10
stripeHeight = 40

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def car2(blockX, blockY):
    gameDisplay.blit(carImg2, (blockX, blockY))

def text_objects(text, font):
    textSurf = font.render(text, True, red)
    return textSurf, textSurf.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((sWidth / 2), (sHeight / 2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

    time.sleep(3)

    game_loop()

def crash():
    message_display('You Crashed')

def grass(aRight, bRight):
    pygame.draw.rect(gameDisplay, green, (aRight, bRight, grassWidth, grassHeight))

def roadStripe(s1, s2):
    pygame.draw.rect(gameDisplay, yellow, (s1, s2, stripeWidth, stripeHeight))


def game_loop():
    x = (sWidth * 0.45)
    y = (sHeight * 0.8)

    aRight = (sWidth - grassWidth)
    bRight = (sHeight - sHeight)

    s1 = (sWidth * 0.46)
    s2 = (sHeight - 80)

    rectX = random.randint(250, 450)
    rectY = - 500
    rectSpeed = 5

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x > 250:
            x -= vel
        if keys[pygame.K_d] and x < 450:
            x += vel
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < sHeight - 80:
            y += vel

        gameDisplay.fill(black)

        grass(aRight - 550, bRight)
        grass(aRight, bRight)

        run = True
        copyStripe = 0
        while run:
            while True:
                roadStripe(s1, s2 - stripeHeight * copyStripe)
                copyStripe += 2
                if copyStripe == 30:
                    break
            s2 += 7
            if s2 - stripeHeight * 12 == sHeight:
                s2 = sHeight - 80
            if s2 - stripeHeight * 12 < sHeight:
                run = False

        car2(rectX, rectY)
        rectY += rectSpeed
        car(x, y)

        if rectY > sHeight:
            rectY = -110
            rectX = random.randint(250, 450)

        if y < rectY + 80 and y > rectY - 80:
            print('Y crossover')
            if x > rectX and x < rectX + 50 or x + 50 > rectX and x + 50 < rectX + 50:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
