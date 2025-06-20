import pygame
from constants import *
from player import *

def main():
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    dt = 0
    
    while True:

        dt_ms = clock.tick(60)
        dt = dt_ms / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        player.update(dt)

        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()
        
if __name__ == '__main__':
    main()