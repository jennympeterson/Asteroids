import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from shot import Shot


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")              

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Player is the name of the class, not an instance of it
# This must be done before any Player objects are created
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)
asteroidfield = AsteroidField()

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

clock = pygame.time.Clock()
dt = 0

running = True
while running:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black") 
    updatable.update(dt)

    for sprite in drawable: #not "player"
        sprite.draw(screen)

    for asteroid in asteroids:
        if player.collides_with(asteroid):
            log_event("player_hit")
            print("Game over!")  
            sys.exit()
        for shot in shots:
            if shot.collides_with(asteroid):
                log_event("asteroid_shot")
                pygame.sprite.Sprite.kill(shot)
                asteroid.split() 

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    print(dt)

if __name__ == "__main__":
    main()
