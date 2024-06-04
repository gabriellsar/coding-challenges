from planet import Planet
from main import SIZE


class Dot(Planet):
    def __init__(self, velocity: tuple, pos: tuple):
        super().__init__(pos, 5, 1)
        self.pos_x, self.pos_y = pos
        self.v_x, self.v_y = velocity
        self.trail = []

    def move(self):
        self.pos_x += self.v_x
        self.pos_y += self.v_y

        if self.pos_x - 1 <= 0 or self.pos_x + 1 >= SIZE[0]:
            self.v_x = -self.v_x
        if self.pos_y - 1 <= 0 or self.pos_y + 1 >= SIZE[1]:
            self.v_y = -self.v_y

        self.trail.append((self.pos_x, self.pos_y))
        if len(self.trail) > 100:
            self.trail.pop(0)

    def apply_force(self, other) -> float:
        pass
        