"""Tento modul obsahuje definici třídy Trojuhelnik."""
import math


class Trojuhelnik:
    """Uchovává atributy trojúhelníku ve 2D prostoru."""

    def __init__(self, bod_a, bod_b, bod_c):
        """
        Konstruktor trojúhelníku.

        :param Bod bod_a: bod vrcholu A
        :param Bod bod_b: bod vrcholu B
        :param Bod bod_c: bod vrcholu C
        """
        self.bod_a = bod_a
        self.bod_b = bod_b
        self.bod_c = bod_c

    @property
    def a(self):
        """Délka strany a."""
        return self.bod_b.vzdalenost_k_bodu(self.bod_c)

    @property
    def b(self):
        """Délka strany b."""
        return self.bod_a.vzdalenost_k_bodu(self.bod_c)

    @property
    def c(self):
        """Délka strany c."""
        return self.bod_a.vzdalenost_k_bodu(self.bod_b)

    def je_sestrojitelny(self):
        """Táto funkcia nám hovorí či je trojuholnik zostrojitelný."""
        return self.a + self.b >= self.c \
            and self.a + self.c >= self.b \
            and self.b + self.c >= self.a

    def obvod(self):
        """Táto funkcia nám vypočíta obvod trojuholníka."""
        return self.a + self.b + self.c

    def obsah(self):
        """Táto funkcia nám vypočíta obsah trojuholníka."""
        return math.sqrt(
            self.obvod() / 2 * (self.obvod() / 2 - self.a) * (self.obvod() / 2 - self.b) * (self.obvod() / 2 - self.c))

    def je_pravouhly(self):
        """Táto funkcia nám zistí, či je trojuholník pravouhlý."""
        return self.c ** 2 == self.a ** 2 + self.b ** 2 \
            or self.a ** 2 + self.c ** 2 == self.b ** 2 \
            or self.b ** 2 + self.c ** 2 == self.a ** 2
