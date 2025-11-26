import pygame
import sys

pygame.init()

SCREEN_W = 600
SCREEN_H = 600
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = SCREEN_W / 2, SCREEN_H - 140 * SCREEN_H / 800

jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
MARIO_RUNNING = pygame.transform.scale(pygame.image.load("assets/mario_running.png"), (48, 64))
mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))
BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND =pygame.transform.scale(BACKGROUND, (SCREEN_W, SCREEN_H))

bg_width = BACKGROUND.get_width()

x_offset = 0
while True:

    speed = 1
    
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
        
            
    # faster speed mode
    if keys_pressed[pygame.K_LSHIFT]:
        speed *= 4 
    
    # While loop piirtää taustan kapeista suikaleista
    # jotta voidaan scrollata left/right
    x_offset += speed
    x = -(x_offset % bg_width)
    mario_rect = mario_rect.move(speed / 2, 0)    

    while x < SCREEN_W:
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