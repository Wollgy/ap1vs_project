"""Obsahuje Unit testy pro modul bod."""
from unittest import TestCase
from bod import Bod
from trojuhelnik import Trojuhelnik


class TestTrojuhelnik(TestCase):
    """Spouští testy funkcí pro práci s trojúhelníkem."""

    def test_je_sestrojitelny(self):
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        message = "Nejde zostrojit."
        self.assertTrue(
            trojuhelnik.je_sestrojitelny(), message)

    def test_je_sestrojitelny_neplati(self):
        trojuhelnik = Trojuhelnik(Bod(0, 2), Bod(0, 2), Bod(2, 5))
        message = "Ide zostrojit."
        self.assertFalse(
            trojuhelnik.je_sestrojitelny(), message)

    def test_obvod(self):
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertEqual(
            round(trojuhelnik.obvod(), 3), 7.256)

    def test_obvod_nevyjde(self):
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertNotEqual(
            round(trojuhelnik.obvod(), 3), 7)

    def test_obsah(self):
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertEqual(
            round(trojuhelnik.obsah(), 3), 0.5)

    def test_fobsah(self):
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertNotEqual(
            round(trojuhelnik.obsah(), 3), 1)

    def test_je_pravouhly(self):
        message = "Nie je pravouhly."
        trojuhelnik = Trojuhelnik(Bod(0, 0), Bod(9, 0), Bod(0, 9))
        self.assertTrue(trojuhelnik.je_pravouhly(), message)

    def test_nieje_pravouhly(self):
        message = "Je pravouhly."
        trojuhelnik = Trojuhelnik(Bod(1, 6), Bod(2, 8), Bod(3, 9))
        self.assertFalse(trojuhelnik.je_pravouhly(), message)
