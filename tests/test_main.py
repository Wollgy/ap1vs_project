"""Obsahuje Unit testy pro modul main."""
from unittest import TestCase
import main
import unittest.mock as mock
import sys
import random
import io


class TestMain(TestCase):
    """Spouští testy funkcí v hlavním modulu."""

    def test_ziskej_souradnice_bodu_platne(self):
        """Ověření úspěšného vytvoření bodu ze správně zadaných souřadnic."""
        sys.stdout = io.StringIO()
        x = random.uniform(-20, 20)
        y = random.uniform(-20, 20)
        with mock.patch("builtins.input", lambda *args: f" {x} {y} "):
            bod = main.ziskej_souradnice_bodu("X")
            assert bod.x == x and bod.y == y
            sys.stdout = sys.stdout

    def test_ziskej_souradnice_bodu_nespravny_pocet(self):
        """Ověření, zda funkce rozpozná nesprávný počet souřadnic."""
        sys.stdout = io.StringIO()
        x = random.uniform(-20, 20)
        y = random.uniform(-20, 20)
        z = random.uniform(-20, 20)
        with mock.patch("builtins.input", lambda *args: f"{x} {y} {z}"):
            bod = main.ziskej_souradnice_bodu("X")
            self.assertIsNone(bod)
            sys.stdout = sys.stdout

    def test_ziskej_souradnice_bodu_nespravna_hodnota(self):
        """Ověření vyvolání chyby při zadání nenumerické hodnoty."""
        sys.stdout = io.StringIO()
        with mock.patch("builtins.input", lambda *args: "x y"):
            main.ziskej_souradnice_bodu("X")
            self.assertRaises(ValueError)
            sys.stdout = sys.stdout
