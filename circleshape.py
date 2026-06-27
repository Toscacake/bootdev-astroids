import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other) -> bool:
        if self.position.distance_to(other.position) > self.radius * 2:
            return False
        else:
            return True

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        pygame.draw.polygon(self.screen, "white", self.triangle(), self.radius)
        pass

    def update(self, dt: float) -> None:
        # must override
        pass