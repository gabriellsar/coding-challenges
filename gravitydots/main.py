import pygame as pg
from bola import *

pg.init()

dimensions = (16*25, 9*25)
janela = pg.display.set_mode(dimensions, pg.NOFRAME)
pg.display.set_caption('Dots')
clock = pg.time.Clock()

bolas = []

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = event.pos

            cor = color_gradient()
            bolas.append(Bola(pos, cor))
    janela.fill((0, 0, 0))

    for bola in bolas:
        bola.mover(dimensions[0], dimensions[1])
        bola.applicator_force(bolas)
        bola.draw_ball(janela)
    pg.display.flip()
    clock.tick(144)

pg.quit()
