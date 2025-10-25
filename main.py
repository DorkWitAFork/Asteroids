# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()
    

    Player.containers           = (updatable, drawable)
    Asteroid.containers         = (asteroids, updatable, drawable)
    AsteroidField.containers    = (updatable,)
    Shot.containers             = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # main game loop 
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        dt = clock.tick(60) / 1000

        for fella in drawable:
            fella.draw(screen)

        for smella in updatable:
            smella.update(dt)

        for asteroid in asteroids:
            
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()

            if asteroid.collide(player):
                print("Game over!")
                sys.exit()

        # player.draw(screen)
        # player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
