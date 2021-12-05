"""Tento modul obsahuje definici třídy Bod."""
import math


class Bod:
    """Uchovává souřadnice bodu ve 2D prostoru na osách x a y."""

    def __init__(self, x, y):
        """
        Konstruktor bodu ve 2D prostoru.

        :param x: souřadnice bodu na ose x
        :param y: souřadnice bodu na ose y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Vrací reprezentaci bodu (jeho souřadnice) jako řetězec.

        :rtype: str
        :return: řetězec se souřadnicemi bodu ve formátu (x;y)
        """
        return f"({self.x};{self.y})"

    def vzdalenost_k_bodu(self, bod):
        """
        Vrací vzdálenost mezi tímto a zadaným bodem.

        K výpočtu se využívá vzorec pro velikost vektoru.

        :param bod: druhý bod v prostoru, k němuž se zjišťuje vzdálenost
        :rtype: float
        :return: vzdálenost mezi tímto a zadaným bodem
        """
        return math.sqrt((self.x - bod.x)**2 + (self.y - bod.y)**2)
