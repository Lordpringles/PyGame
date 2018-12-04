import pygame
import time
import random

pygame.init()

screen_width = 800
screen_height = 600
display = (screen_width, screen_height)
display_size = pygame.display.set_mode(display)
pygame.display.set_caption('Jet Game')
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (0, 255, 255)
purple = (255, 0, 255)
orange = (255, 255, 0)

jet_width = 150
jet_height = 50
jet_speed = 5
cloud_width = 200
cloud_height = 100
cloud_speed = 10
shoot_width = 10
shoot_height = 10
shoot_speed = 15
enemy_speed = 5

jet_img = pygame.image.load('jet.png')
jet_img = pygame.transform.scale(jet_img, (jet_width, jet_height))
enemy_jet = pygame.image.load('enemy_jet.png')
enemy_jet = pygame.transform.scale(enemy_jet, (jet_width, jet_height))
cloud_img = pygame.image.load('cloud.png')
cloud_img = pygame.transform.scale(cloud_img, (cloud_width, cloud_height))


def jet(x, y):
    display_size.blit(jet_img, (x, y))

def enemy(enemy_x, enemy_y):
    display_size.blit(enemy_jet, (enemy_x, enemy_y))


def shoot(shoot_x, shoot_y):
    pygame.draw.rect(display_size, red, (shoot_x, shoot_y, shoot_width, shoot_height))


def cloud1(cloud1X, cloud1Y):
    display_size.blit(cloud_img, (cloud1X, cloud1Y))

def cloud2(cloud2X, cloud2Y):
    display_size.blit(cloud_img, (cloud2X, cloud2Y))

def cloud3(cloud3X, cloud3Y):
    display_size.blit(cloud_img, (cloud3X, cloud3Y))

def game_loop():

    x = 0
    y = (screen_height / 2.5)

    enemy_x = screen_width + 300
    enemy_y = random.randint(0, screen_height - jet_height)

    shoot_x = x + jet_width - 10
    shoot_y = y + jet_height / 2
    shoot_count = 0

    cloud1X = screen_width + cloud_width * 3
    cloud1Y = random.randint(0, screen_height - cloud_height)

    cloud2X = screen_width + cloud_width
    cloud2Y = random.randint(0, screen_height - cloud_height)

    cloud3X = screen_width + cloud_width * 5
    cloud3Y = random.randint(0, screen_height - cloud_height)

    crash = False
    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True

        display_size.fill(lightblue)
        cloud3(cloud3X, cloud3Y)
        cloud3X -= cloud_speed
        cloud2(cloud2X, cloud2Y)
        cloud2X -= cloud_speed
        cloud1(cloud1X, cloud1Y)
        cloud1X -= cloud_speed
        jet(x, y)
        enemy(enemy_x, enemy_y)
        enemy_x -= enemy_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x > -10:
            x -= jet_speed
        if keys[pygame.K_d] and x < screen_width - jet_width + 10:
            x += jet_speed
        if keys[pygame.K_w] and y > -10:
            y -= jet_speed
        if keys[pygame.K_s] and y < screen_height - jet_height + 10:
            y += jet_speed
        if keys[pygame.K_SPACE] and enemy_y != 9000:
            shoot_count += 1
        if shoot_count != 0:
            shoot(shoot_x, shoot_y)
            shoot_x += shoot_speed
            if shoot_x > screen_width + shoot_width:
                shoot_count = 0
        else:
            shoot_x = x + jet_width - 10
            shoot_y = y + jet_height / 2

        if cloud3X < 0 - cloud_width:
            cloud3X = screen_width + cloud_width
            cloud3Y = random.randint(0, screen_height - cloud_height)
        if cloud2X < 0 - cloud_width:
            cloud2X = screen_width + cloud_width
            cloud2Y = random.randint(0, screen_height - cloud_height)
        if cloud1X < 0 - cloud_width:
            cloud1X = screen_width + cloud_width
            cloud1Y = random.randint(0, screen_height - cloud_height)
        if enemy_x == 0 - jet_width:
            enemy_x = screen_width + jet_width
            enemy_y = random.randint(0, screen_height - jet_height)

        if shoot_x >= enemy_x + 10 and shoot_x + shoot_width <= enemy_x + jet_width - 10:
            if shoot_y >= enemy_y + 10 and shoot_y + shoot_height - 10 <= enemy_y + jet_height - 10 and shoot_x != x + jet_width -10 or shoot_y + shoot_height >= enemy_y and shoot_y <= enemy_y + jet_height - 10 and shoot_x != x + jet_width - 10:
                enemy_y = 9000
                enemy_x = -100
                shoot_count = 0

        pygame.display.update()
        clock.tick(60)


game_loop()

pygame.quit()