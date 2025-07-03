import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    
    dt = 0
    
    while True:

        dt_ms = clock.tick(60)
        dt = dt_ms / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
        
        screen.fill('black')
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
if __name__ == '__main__':
    main()