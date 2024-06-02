from math import sqrt
from circle import Circle
from complex import Complex


def descartes(c1: Circle, c2: Circle, c3: Circle) -> list[float]:
    soma: float = c1.bend + c2.bend + c3.bend
    produto = abs(c1.bend * c2.bend + c3.bend * c1.bend + c2.bend * c3.bend)
    root: float = 2 * sqrt(produto)

    return [soma + root, abs(soma - root)]


def complex_descartes(c1: Circle, c2: Circle, c3: Circle, k4: list) -> list[Circle]:
    k1, k2, k3 = c1.bend, c2.bend, c3.bend
    z1, z2, z3 = c1.center, c2.center, c3.center

    zk1 = z1.scale(k1)
    zk2 = z2.scale(k2)
    zk3 = z3.scale(k3)
    soma = zk1.add(zk2).add(zk3)

    root = Complex.c_sqrt(zk1.multiply(zk2).add(zk1.multiply(zk3)).add(zk2.multiply(zk3)))
    root = root.scale(2.0)

    center1 = soma.add(root).scale(1 / k4[0])
    center2 = soma.subtract(root).scale(1 / k4[0])
    center3 = soma.add(root).scale(1 / k4[1])
    center4 = soma.subtract(root).scale(1 / k4[1])

    return [Circle(center1.real, center1.imaginary, k4[0]),
            Circle(center2.real, center2.imaginary, k4[0]),
            Circle(center3.real, center3.imaginary, k4[1]),
            Circle(center4.real, center4.imaginary, k4[1])
            ]
