import pygame
import random

pygame.init()



screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("game test")

# 플레이어
x = 50
y = 50
width = 20
height = 20
vel = 5

# 적
x1 = random.randrange(100,screenHeight)
y1 = random.randrange(100,screenWidth) # 랜덤한 위치에서 생성


run = True
while run:
    pygame.time.delay(15)

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



    # 적 움직임
    pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))
    rand = random.randrange(0,4)

    if rand == 1 and x1 > vel:
        x1 -= vel
    if rand == 2 and x1 < screenWidth - width - vel:
        x1 += vel
    if rand == 3 and y1 > vel:
        y1 -= vel
    if rand == 4 and y1 < screenHeight - height - vel:
        y1 += vel

    distance = ( (x1 - x)**2 + (y1 - y)**2 ) ** 0.5
    
    if (distance < 20):
        print("game over")
        run = False




    
    pygame.display.update()

pygame.quit()
