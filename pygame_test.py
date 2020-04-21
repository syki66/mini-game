import pygame

pygame.init()


screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("game test")

x = 50
y = 50
width = 30
height = 30
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
        y += vel
    if keys[pygame.K_SPACE]:
       isJump = True
            
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
