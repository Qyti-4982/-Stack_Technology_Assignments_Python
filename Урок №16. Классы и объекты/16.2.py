
import math

class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        if s <= 0:
            raise ValueError("Количество клеточек должно быть выше нуля!")
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        return self.x, self.y, self.s 
    
    def go_down(self):
        self.y -= self.s
        return self.x, self.y, self.s 
    
    def go_left(self):
        self.x -= self.s
        return self.x, self.y, self.s

    def go_right(self):
        self.x += self.s
        return self.x, self.y, self.s

    def evolve(self):
        self.s += 1
        return self.s
    
    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Нельзя уменшить s - оно станет <= 0")
        self.s -= 1
        return self.s

    def count_moves(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        dx = abs(x2 - self.x )
        dy = abs(y2 - self.y)
        moves_x = math.ceil(dx / self.s if self.s > 0 else float("inf"))
        moves_y = math.ceil(dy / self.s if self.s > 0 else float("inf"))
        return max(moves_x, moves_y)
    
черепашка = Черепашка()
K = (input("Введите команду(go_up - вверх, go_down - вниз, go_left - налево, go_right - направо, evolve - увеличение шага, degrade - уменьшение шага, count_moves - расчёт количество шагов от текущей до заданной позиции): "))
while (K != "stop"):
    if K == "go_up":
        go_up_ = черепашка.go_up()
        print(go_up_)
    elif K == "go_down":
        go_down_ = черепашка.go_down();
        print(go_down_)
    elif K == "go_left":
        go_left_ = черепашка.go_left()
        print(go_left_)
    elif K == "go_right":
        go_right_ = черепашка.go_right()
        print(go_right_)
    elif K == "evolve":
        evolve_ = черепашка.evolve()
        print(evolve_)
    elif K == "degrade":
        degrade_ = черепашка.degrade()
        print(degrade_)
    elif K == "count_moves":
        x2 = int(input("Введите целевую позицию по x: "))
        y2 = int(input("Введите целевую позицию по y: "))
        count_moves_ = черепашка.count_moves(x2, y2)
        print(count_moves_)
    else: print("Указанной команды не существует!")
    K = (input("Введите команду(go_up - вверх, go_down - вниз, go_left - налево, go_right - направо, evolve - увеличение шага, degrade - уменьшение шага, count_moves - расчёт количество шагов от текущей до заданной позиции): "))
