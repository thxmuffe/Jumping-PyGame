import pygame
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = 400, 660

jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
MARIO_RUNNING = pygame.transform.scale(pygame.image.load("assets/mario_running.png"), (48, 64))
mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))
BACKGROUND = pygame.image.load("assets/background.png")

bg_width = BACKGROUND.get_width()

x_offset = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    # jumping
    if keys_pressed[pygame.K_SPACE] and not jumping:
        jumping = True
        start_rect = mario_rect
        Y_VELOCITY = JUMP_HEIGHT
    
    # moving left/right
    if keys_pressed[pygame.K_LEFT]:
        speed = -1
    elif keys_pressed[pygame.K_RIGHT]:
        speed = +1
    else:
        speed = 0
            
    # faster speed mode
    if keys_pressed[pygame.K_LSHIFT]:
        speed *= 4 
    
    # While loop piirtää taustan kapeista suikaleista
    # jotta voidaan scrollata left/right
    x_offset += speed
    x = -(x_offset % bg_width)
    mario_rect = mario_rect.move(speed / 2, 0)    
    while x < 800:
        SCREEN.blit(BACKGROUND, (x, 0))
        x += bg_width
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        if Y_POSITION > start_rect.bottom:
            jumping = False
            mario_rect = start_rect
    
    if jumping:
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
    elif abs(speed) > 1:
        SCREEN.blit(MARIO_RUNNING, mario_rect)  
    else:
        SCREEN.blit(STANDING_SURFACE, mario_rect)
        
    pygame.display.update()
    CLOCK.tick(60)