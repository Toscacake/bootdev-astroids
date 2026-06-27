import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from player import Player
from shot import Shot
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
# INITIERING AV VARIABLER
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    #asteroids = Asteroid()

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updatable)

# GAME-LOOP, KÖRS KONTINUELIGT
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fyll skärm
        screen.fill("black")

        # Uppdatera objekt i upd/draw -grupper
        dt = clock.tick(60) / 1000
        for thing in updatable:
            thing.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")  
                        asteroid.split()
                        shot.kill()
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\n Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
