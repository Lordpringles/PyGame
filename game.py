import pygame
pygame.init()

sWidth = 800
sHeight = 600

window = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('Test')

x = 0
y = 470
cWidth = 50
cHeight = 80
fWidth = 800
fHeight = 50
vel = 10
isJump = False
jumpCount = 8

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8

    pygame.draw.rect(window, (0, 255, 0), (x, y, cWidth, cHeight))
    pygame.draw.rect(window, (255, 0, 0), (0, 550, fWidth, fHeight))
    pygame.display.update()
    window.fill((0, 0, 0))

pygame.quit()