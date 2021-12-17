import pygame

MAX_X = 1920
MAX_Y = 1080
game_over = False

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("hello my First Pygame")

print(pygame.image.get_extended())


myimage = pygame.image.load("matrix-reloaded-fashion-model-beauty-monica-bellucci-long-hair.jpg").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 500
y = 100

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20



    screen.blit(myimage, (500, 100))
    pygame.display.flip()

