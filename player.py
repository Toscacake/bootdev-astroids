from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # self.x = x
        # self.y = y
        self.rotation = 0
        #CircleShape(self.x, self.y, PLAYER_RADIUS)


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]