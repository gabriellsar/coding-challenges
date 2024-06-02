from time import sleep

from p5 import *
from random import randint
from circle import Circle
import apollianFractal as apfr

tam = 400
pos = tam // 2

allCircles: list[Circle] = []
Queue = []
epsilon = 0.1


def setup():
    size(tam, tam)  # Size should be the first statement
    c1: Circle = Circle(pos, pos, -1 / 200)

    r2 = randint(10, c1.radius / 2)

    pos_vector = Vector(1, 1).random_2D()
    pos_vector.magnitude = c1.radius - r2
    c2: Circle = Circle(pos + pos_vector.x, pos + pos_vector.y, 1 / r2)

    r3 = pos_vector.mag()
    pos_vector.rotate(PI)
    pos_vector.magnitude = c1.radius - r3
    c3: Circle = Circle(pos + pos_vector.x, pos + pos_vector.y, 1 / r3)

    allCircles.append(c1)
    allCircles.append(c2)
    allCircles.append(c3)

    Queue.append([c1, c2, c3])


def is_tangent(c1, c2):
    d = c1.dist(c2)
    r1 = c1.radius
    r2 = c2.radius

    a = abs(d - (r1 + r2)) < epsilon
    b = abs(d - abs(r2 - r1)) < epsilon
    return a or b


def circle_is_valid(c4: Circle, c1, c2, c3) -> bool:
    if c4.radius < 4:
        return False

    for other in allCircles:
        dis = c4.dist(other)
        rad_diff = abs(c4.radius - other.radius)
        if dis < epsilon and rad_diff < epsilon: return False

    if not is_tangent(c4, c1): return False
    if not is_tangent(c4, c2): return False
    if not is_tangent(c4, c3): return False
    return True


def next_generation():
    global Queue
    next_queue = []

    for t in Queue:
        c1, c2, c3 = t
        k4 = apfr.descartes(c1, c2, c3)
        new_circles: list[Circle] = apfr.complex_descartes(c1, c2, c3, k4)
        for c in new_circles:
            if circle_is_valid(c, c1, c2, c3):
                allCircles.append(c)
                ts = [[c1, c2, c], [c1, c3, c], [c2, c3, c]]
                for T in ts:
                    next_queue.append(T)
    Queue = next_queue


def draw():
    background(20)
    next_generation()

    for c in allCircles:
        c.show()


if __name__ == '__main__':
    run()
