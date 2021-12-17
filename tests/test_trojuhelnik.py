"""Obsahuje Unit testy pro modul bod."""
from unittest import TestCase
from bod import Bod
from trojuhelnik import Trojuhelnik


class TestTrojuhelnik(TestCase):
    """Spouští testy funkcí pro práci s trojúhelníkem."""

    def test_je_sestrojitelny(self):
        """Overenie sestrojitelnosti trojuholnika."""
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        message = "Nejde zostrojit."
        self.assertTrue(
            trojuhelnik.je_sestrojitelny(), message)

    def test_je_sestrojitelny_neplati(self):
        """Overenie nesestrojitelnosti trojuholnika."""
        trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
        message = "Ide zostrojit."
        self.assertFalse(
            trojuhelnik.je_sestrojitelny(), message)

    def test_obvod(self):
        """Overenie rovnosti obvodu."""
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertEqual(
            round(trojuhelnik.obvod(), 3), 7.256)

    def test_obvod_nevyjde(self):
        """Overenie nerovnosti obvodu."""
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertNotEqual(
            round(trojuhelnik.obvod(), 3), 7)

    def test_obvod_neplatneho_trojuhelniku(self):
        """Overenie vyvolania vynimky."""
        with self.assertRaises(Exception):
            trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
            trojuhelnik.obvod()

    def test_obsah(self):
        """Overenie rovnosti obsahu."""
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertEqual(
            round(trojuhelnik.obsah(), 3), 0.5)

    def test_obsah_nevyjde(self):
        """Overenie nerovnosti obsahu."""
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertNotEqual(
            round(trojuhelnik.obsah(), 3), 1)

    def test_obsah_neplatneho_trojuhelniku(self):
        """Overenie vyvolania vynimky trojuholnika."""
        with self.assertRaises(Exception):
            trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
            trojuhelnik.obsah()

    def test_je_pravouhly(self):
        """Overenie pravouhlosti trojuholnika."""
        message = "Nie je pravouhly."
        trojuhelnik = Trojuhelnik(Bod(0, 0), Bod(9, 0), Bod(0, 9))
        self.assertTrue(trojuhelnik.je_pravouhly(), message)

    def test_je_pravouhly_neplati(self):
        """Overenie nepravouhlosti."""
        message = "Je pravouhly."
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertFalse(trojuhelnik.je_pravouhly(), message)

    def test_pravouhlost_neplatneho_trojuhelniku(self):
        """Overenie vyvolania vynimky."""
        with self.assertRaises(Exception):
            trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
            trojuhelnik.je_pravouhly()

    def test_pravouhlost_neplatneho_trojuhelniku(self):
        """Overenie vyvolania vynimky trojuholnika."""
        with self.assertRaises(Exception):
            trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
            trojuhelnik.je_pravouhly()
