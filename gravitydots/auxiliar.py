from pygame import Surface, draw, SRCALPHA
from random import random


def color_gradient() -> tuple:
    r = int(255 * random())
    return r, 0, 255 - r


def draw_shine_ball(surface, cor, pos, raio):
    for i in range(raio, raio * 4, raio):

        layer = Surface((i * 2, i * 2), SRCALPHA)
        transparency = 255 - (255 * (i - raio) // (3 * raio))
        layer_color = (*cor, transparency)

        draw.circle(layer, layer_color, (i, i), i)
        surface.blit(layer, (pos[0] - i, pos[1] - i))
