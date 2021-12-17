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
        sys.stdout = io.StringIO()  # potlačení print outputu
        x = random.uniform(-20, 20)
        y = random.uniform(-20, 20)
        with mock.patch("builtins.input", lambda *args: f" {x} {y} "):
            bod = main.ziskej_souradnice_bodu("X")
            assert bod.x == x and bod.y == y
        sys.stdout = sys.stdout  # obnovení print outputu

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

    def test_spust_trojuhelnik_spravne_argumenty(self):
        """Ověří úspěšnost programu se správnými argumenty z terminálu."""
        sys.stdout = io.StringIO()
        with mock.patch.object(sys, "argv",
                               ["main.py", "1", "2", "3", "4", "5", "6"]):
            with self.assertRaises(SystemExit) as se:
                main.spust_trojuhelnik()
            self.assertEqual(se.exception.code, 0)  # exit code check
        sys.stdout = sys.stdout

    def test_spust_trojuhelnik_nespravny_pocet_argumentu(self):
        """Ověří neúspěšnost programu při nesprávném počtu argumentů."""
        sys.stdout = io.StringIO()
        with mock.patch.object(sys, "argv", ["main.py", "1", "2", "3"]):
            with self.assertRaises(SystemExit) as se:
                main.spust_trojuhelnik()
            self.assertEqual(se.exception.code, 1)
        sys.stdout = sys.stdout

    def test_spust_trojuhelnik_nenumericke_argumenty(self):
        """Ověří neúspěšnost programu při nenumerických argumentech."""
        sys.stdout = io.StringIO()
        with mock.patch.object(sys, "argv",
                               ["main.py", "1", "2", "3", "4", "5", "abc"]):
            with self.assertRaises(SystemExit) as se:
                main.spust_trojuhelnik()
            self.assertEqual(se.exception.code, 1)
        sys.stdout = sys.stdout

    def test_spust_trojuhelnik_bez_argumentu(self):
        """Ověří úspěšnost programu při spuštění bez argumentů."""
        sys.stdout = io.StringIO()
        with mock.patch.object(sys, "argv", ["main.py"]):
            mock_args = ["1 2", "3 4", "5 6"]
            with mock.patch("builtins.input", side_effect=mock_args):
                with self.assertRaises(SystemExit) as se:
                    main.spust_trojuhelnik()
                self.assertEqual(se.exception.code, 0)
        sys.stdout = sys.stdout
