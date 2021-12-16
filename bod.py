"""Tento modul obsahuje definici třídy Bod."""
import math


class Bod:
    """Uchovává souřadnice bodu ve 2D prostoru na osách x a y."""

    def __init__(self, x, y):
        """
        Konstruktor bodu ve 2D prostoru.

        :param int|float x: souřadnice bodu na ose x
        :param int|float y: souřadnice bodu na ose y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Vrací reprezentaci bodu (jeho souřadnice) jako řetězec.

        :return: řetězec se souřadnicemi bodu ve formátu [x;y]
        :rtype: str
        """
        return f"[{self.x};{self.y}]"

    def vzdalenost_k_bodu(self, bod):
        """
        Vrací vzdálenost mezi tímto a zadaným bodem.

        :param Bod bod: bod v prostoru, k němuž se zjišťuje vzdálenost
        :return: vzdálenost mezi tímto a zadaným bodem
        :rtype: float
        """
        return math.sqrt((self.x - bod.x) ** 2 + (self.y - bod.y) ** 2)
