# import main library(ies)
import sys
# import pygame library (make sure to install it on your computer)
import pygame
pygame.init()

# initialize pygame objects
screen = pygame.display.set_mode((500, 500))
player = pygame.image.load("./icons/bird.jpg")
playerRect = player.get_rect()
playerRect = (50, 200)

# Pipe Class
class Pipe:
    pass

# Frame Loop
while True:
    # Check for an event
    for event in pygame.event.get():
        # If event = QUIT, close out
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Screen Update
    screen.fill((255, 255, 255))
    screen.blit(player, playerRect)
    pygame.display.flip()
    