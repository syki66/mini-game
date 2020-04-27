import pygame
import random

pygame.init()

screenWidth = 1000
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("game test")

# 플레이어
x = 50 # 플레이어 초기 x 위치값
y = 50 # 플레이어 초기 y 위치값
width = 20 # 플레이어 높이
height = 20 # 플레이어 너비
vel = 5 # 이동속도

# 적
enemyNum = 20 # 적 개수

# 적 위치 값을 배열 넣기, 랜덤한 초기 위치값으로 설정
enemy = []
for i in range(enemyNum):
    enemy.append([random.randrange(100,screenWidth), random.randrange(100,screenHeight)])

run = True
while run:
    pygame.time.delay(15) # 게임 속도조절

    # 윈도우창 끌수 있게끔 하는거
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 키 눌렸을때 설정하는것, 화면 밖으로 못나가게끔 설정함
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
            
    win.fill((0,0,0)) # 각 도형 자취 안남도록 하는것 및 배경설정

    pygame.draw.rect(win, (255,255,255), (x, y, width, height)) # 플레이어 그리기


    # 적 움직임, 우선 랜덤하게 각자 움직이게함
    for i in range(len(enemy)):
        randomColor = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)) # 적 블링블링
        pygame.draw.rect(win, randomColor, (enemy[i][0], enemy[i][1], width, height))
        randomMove = random.randrange(0,4)

        if randomMove == 0 and enemy[i][0] > vel:
            enemy[i][0] -= vel
        if randomMove == 1 and enemy[i][0] < screenWidth - width - vel:
            enemy[i][0] += vel
        if randomMove == 2 and enemy[i][1] > vel:
            enemy[i][1] -= vel
        if randomMove == 3 and enemy[i][1] < screenHeight - height - vel:
            enemy[i][1] += vel

        # 거리가 20 이하로 줄어들면 게임 오버 시킴
        distance = ( (enemy[i][0] - x)**2 + (enemy[i][1] - y)**2 ) ** 0.5 
        if (distance < 20):
            print("game over")
            run = False

    pygame.display.update()

pygame.quit()
