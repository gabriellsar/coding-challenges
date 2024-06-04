# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

SIZE = (1280, 720)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(Bola())

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
