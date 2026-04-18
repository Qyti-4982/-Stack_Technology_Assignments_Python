
import math

class Черепашка:
    def __inite__(self, x=0, y=0, s=1):
        if s <= 0:
            raise ValueError("Количество клеточек должно быть выше нуля!")
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Нельзя уменшить s - оно станет <= 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        dx = abs(x2 - self.x )
        dy = abs(y2 - self.y)
        moves_x = math.ceil(dx / self.s if self.s > 0 else float("inf"))
        moves_y = math.ceil(dy / self.s if self.s > 0 else float("inf"))
        return max(moves_x, moves_y)