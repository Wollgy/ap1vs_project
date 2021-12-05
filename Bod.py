import math


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x};{self.y})"

    def vzdalenost_k_bodu(self, bod):
        return math.sqrt((self.x - bod.x)**2 + (self.y - bod.y)**2)
