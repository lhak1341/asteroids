import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.can_shoot = True

    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)

    def triangle(self):
        f = self.forward()
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + f * self.radius
        b = self.position - f * self.radius - right
        c = self.position - f * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE] and self.can_shoot:
            self.shoot()
            self.can_shoot = False
        if not keys[pygame.K_SPACE]:
            self.can_shoot = True

    def move(self, dt):
        self.position += self.forward() * PLAYER_SPEED * dt

    def shoot(self):
        s = Shot(self.position.x, self.position.y)
        s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED