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
        self.holeY = random.randint(150, 350)
        self.gap = 100 # TODO This should become smaller the farther the inital X is
        self.surface = pygame.image.load("./Python-Flappy-Bird/icons/pipe.png")
        self.rect = self.surface.get_rect()
        self.rect = [self.x, self.holeY + self.gap]

# Initialize Pipe Objects
pipes = []
# for i in range(100):
#     pipes.append(Pipe((i*100)+1000))
pipes.append(Pipe(400))

# Other Initalization
playing = False
debug = False

# Frame Loop
while True:
    # Check for an event
    for event in pygame.event.get():
        # If event = QUIT, close out
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Check for keypress
            # Jump Code
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Check if keypress was space
                playerSpeed = 0.13
            # Start Game
            elif event.key == pygame.K_1:
                playing = True
            # Debug Rotate
            # if event.key == pygame.K_SLASH:
            #     player = pygame.transform.rotate(player, 2)
            #     playerRect = player.get_rect()
            # TODO rotation
            
    
    # Player Events
    
    if playing == True:
        playerSpeed -= 0.00012 
        playerRect[1] -= playerSpeed # Change player Y by ySpeed (the minus equals is bc the higher Y vals are farther down, and I wanted to make ySpeed at least *seem* intuitive)
        if debug == True:
            print(playerRect[1])
        
    
    # Screen Update
    screen.fill((255, 255, 255))
    screen.blit(player, playerRect)
    # Load Pipes
    for i in range(len(pipes)):
        screen.blit(pipes[i].surface, pipes[i].rect)
    # Refresh Screen
    pygame.display.flip()
    