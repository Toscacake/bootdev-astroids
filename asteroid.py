import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_velocity_a = self.velocity.rotate(+angle)
            new_velocity_b = self.velocity.rotate(-angle)
            s_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            s1_asteroid = Asteroid(self.position.x, self.position.y, s_asteroid_radius)
            s2_asteroid = Asteroid(self.position.x, self.position.y, s_asteroid_radius)
            s1_asteroid.velocity = new_velocity_a * 1.2
            s2_asteroid.velocity = new_velocity_b * 1.2


    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    