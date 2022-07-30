# import main library(ies)
import sys, random

# import pygame library (make sure to install it on your computer)
import pygame
pygame.init()

# initialize pygame objects
screen = pygame.display.set_mode((500, 500))
player = pygame.image.load("./Python-Flappy-Bird/icons/bird.jpg")
playerRect = player.get_rect()
playerRect = [50, 200]
playerSpeed = 0

# Pipe Class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 75
        self.holeY = random.randint(75, 425)
        self.gap = 100 # TODO This should become smaller the farther the inital X is
        
    
    def draw(self):
        pass
        # TODO 
        

# Initialize Pipe Objects


# Other Initalization
playing = False

# Frame Loop
while True:
    # Check for an event
    for event in pygame.event.get():
        # If event = QUIT, close out
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Check for keypress
            # Jump Code
            if event.key == pygame.K_SPACE: # Check if keypress was space
                playerSpeed = 0.1   # TODO balancing w/ gravity (force set is bc of feeling of playing flappy bird)
            # Start Game
            elif event.key == pygame.K_1:
                playing = True
            
    
    # Player Events
    
    if playing == True:
        playerSpeed -= 0.0001 # TODO gravity (balancing)
    playerRect[1] -= playerSpeed # Change player Y by ySpeed (the minus equals is bc the higher Y vals are farther down, and I wanted to make ySpeed at least *seem* intuitive)
    
    # Screen Update
    screen.fill((255, 255, 255))
    screen.blit(player, playerRect)
    pygame.display.flip()
    