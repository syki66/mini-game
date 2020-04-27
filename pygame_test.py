import pygame
import random

pygame.init()

screenWidth = 1000
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("game test")

# 플레이어
x = 50 # 플레이어 초기 x 위치값
y = 400 # 플레이어 초기 y 위치값
width = 40 # 플레이어 높이
height = 40 # 플레이어 너비
vel = 1 # 이동속도
jumpHeight = 8 # 점프 높이

# 적
enemyNum = 20 # 적 개수

# 적 위치 값을 배열 넣기, 랜덤한 초기 위치값으로 설정
enemy = []
for i in range(enemyNum):
    enemy.append([ x+(width*random.randrange(5,1000)) , y-(height*random.randrange(0,4)) ])

isJump = False
jumpCount = jumpHeight

pygame.time.delay(10000)

run = True
while run:
    pygame.time.delay(15) # 게임 속도조절

    # 윈도우창 끌수 있게끔 하는거
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # 점프
    if isJump == False:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -jumpHeight:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = jumpHeight
  
    win.fill((0,0,0)) # 각 도형 자취 안남도록 하는것 및 배경설정

    pygame.draw.rect(win, (255,255,255), (x, y, width, height)) # 플레이어 그리기

    # 적 움직임, 우선 랜덤하게 각자 움직이게함
    for i in range(len(enemy)):
        pygame.draw.rect(win, (255,0,0), (enemy[i][0], enemy[i][1], width, height))

        enemy[i][0] -= vel

        # 거리가 20 이하로 줄어들면 게임 오버 시킴
        distance = ( (enemy[i][0] - x)**2 + (enemy[i][1] - y)**2 ) ** 0.5 
        if (distance < width):
            if enemy[i][1] < x:
                y += enemy[i][1]
            else:
                print("game over")
                run = False

    pygame.display.update()

pygame.quit()
