from settings import *
from random import choice, randint


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, ball_sprites):
        super().__init__(groups)
        self.ball_sprites = ball_sprites

        # image
        self.image = pygame.Surface(BALL_SIZE, pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_SIZE[0]/2, BALL_SIZE[1]/2), BALL_SIZE[0]/2)

        # circle & movement
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2(choice((-1, 1)), choice((-1, 1)))

    def move(self, dt):
        self.rect.center += self.direction * BALL_SPEED * dt

    def collision(self, direction):
        for sprite in self.ball_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.rect.right > sprite.rect.left and self.old_rect.righ >= sprite.old_rect.right:
                        self.rect.right = sprite.rect.left

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1

    def update(self, dt):
        self.move(dt)
        self.wall_collision()
