"""Tento modul obsahuje definici třídy Trojuhelnik."""
import math


class Trojuhelnik:
    """Poskytuje funkce pro práci s trojúhelníkem ve 2D prostoru."""

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
        """
        Táto funkcia nám hovorí či je trojuholnik zostrojitelný.

        :return: True, pokud je sestrojitelný, jinak False
        :rtype: bool
        """
        return self.a + self.b > self.c \
            and self.a + self.c > self.b \
            and self.b + self.c > self.a

    def obvod(self):
        """
        Táto funkcia nám vypočíta obvod trojuholníka.

        :return: součet všech stran trojúhelníku
        :rtype: float
        """
        return self.a + self.b + self.c

    def obsah(self):
        """
        Táto funkcia nám vypočíta obsah trojuholníka.

        :return: obsah plochy trojúhelníku
        :rtype: float
        """
        s = self.obvod() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def je_pravouhly(self):
        """
        Táto funkcia nám zistí, či je trojuholník pravouhlý.

        :return: True, pokud je pravoúhlý, jinak False
        :rtype: bool
        """
        pow_a = self.a ** 2
        pow_b = self.b ** 2
        pow_c = self.c ** 2
        return math.isclose(pow_c, pow_a + pow_b) \
            or math.isclose(pow_b, pow_a + pow_c) \
            or math.isclose(pow_a, pow_b + pow_c)
