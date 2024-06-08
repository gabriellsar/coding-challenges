from settings import *
from sprites import Ball


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Planets")
        self.clock = pygame.time.Clock()
        self.running = True

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.ball_sprite = pygame.sprite.Group()
        self.ball = Ball(self.all_sprites, self.ball_sprite)
        self.ball2 = Ball(self.all_sprites, self.ball_sprite)


    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
