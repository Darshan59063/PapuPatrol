import pygame
import random

pygame.mixer.init()

pygame.init()

bgimg = pygame.image.load('bg.png')
bgimg = pygame.display.set_mode((900, 600)).convert_alpha()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
past = 0
# Game Title
pygame.display.set_caption("Patrol Game")
logo = pygame.image.load('papulogo.png')
pygame.display.set_icon(logo)
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Player picture and coordinates
playerImg = pygame.image.load('papu 2.png')
playerX = 450
playerY = 470
velocity_x = 0
velocity_y = 0
init_velocity = 7

# Player picture and coordinates
bvelocity_y = 5

beer1 = pygame.image.load('beer.png')
beer1X = random.randint(200, 550)
beer1Y= 25


beer2 = pygame.image.load('beer.png')
beer2X = random.randint(200, 550)
beer2Y= 10

score = 0
# Game specific variables
exit_game = False
game_over = False
fps = 30
def beer1fY():
    global beer1Y
    gameWindow.blit(beer1, (beer1X, beer1Y))
    beer1Y += bvelocity_y
def beer2fY():
    global beer2Y
    gameWindow.blit(beer2, (beer2X, beer2Y))
    beer2Y += bvelocity_y
def player():
    gameWindow.blit(playerImg, (playerX,playerY))

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])







while not exit_game:
    if playerX < 0:
        playerX = 0
    elif playerX > 820:
        playerX = 820


    if game_over:

        gameWindow.fill(white)
        text_screen("Game Over! Press Enter To Continue", red, 100, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity

                if event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity
        pygame.mixer.music.load('papu.mp3')
        pygame.mixer.music.play()

        playerX = playerX + velocity_x
        playerY = playerY + velocity_y

        gameWindow.fill(white)
        gameWindow.blit(bgimg, (0, 0))
        player()
        beer1fY()
        if  beer1Y == 200:
            past = 1;
        elif past == 1:
            beer2fY()
        if abs(playerX - beer1X)<=60 and abs(playerY - beer1Y)<=80:
            beer1Y = 0
            beer1X = random.randint(200, 550)
            beer1fY()
            score = score + 10
        elif abs(playerX - beer1X)>60 and abs(playerY - beer1Y)<=80:
            game_over = True

        if abs(playerX - beer2X)<=60 and abs(playerY - beer2Y)<=80:
            beer2Y = 0
            beer2X = random.randint(200, 550)
            beer2fY()
            score = score + 10
        elif abs(playerX - beer2X)>60 and abs(playerY - beer2Y)<=80:
            game_over = True

        text_screen("Score: " + str(score), red, 5, 5)


        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()