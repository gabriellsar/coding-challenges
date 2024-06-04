from auxiliar import *
import math


class Bola:
    def __init__(self, pos: tuple, cor: tuple):
        self.x, self.y = pos
        self.cor = cor
        self.raio = 5
        self.vel_x, self.vel_y = 3, 0
        self.trail = []

    def mover(self, lar: int, alt: int):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x - self.raio <= 0 or self.x + self.raio >= lar:
            self.vel_x = -self.vel_x

        if self.y - self.raio <= 0 or self.y + self.raio >= alt:
            self.vel_y = -self.vel_y

        self.trail.append((self.x, self.y))
        if len(self.trail) > 50:  # Limit the size of the trail
            self.trail.pop(0)

    def distance(self, ball):
        dx = ball.x - self.x
        dy = ball.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance, dx, dy

    def applicator_force(self, balls):
        G = 6.67  # Gravitational Constant
        for ball in balls:
            if ball != self:
                dist, dx, dy = self.distance(ball)
                if dist > 0:
                    force = G * (self.raio * ball.raio) / (dist ** 2)
                    angle = math.atan2(dy, dx)

                    self.vel_x += math.cos(angle) * force
                    self.vel_y += math.sin(angle) * force
        self.vel_x = max(min(self.vel_x, 3), -3)
        self.vel_y = max(min(self.vel_y, 3), -3)

    def draw_ball(self, surface: Surface):
        if len(self.trail) > 1:
            draw.lines(surface, self.cor, False, self.trail, 5)
        draw_shine_ball(surface, self.cor, (self.x, self.y), self.raio)
