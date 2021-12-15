"""Obsahuje Unit testy pro modul bod."""
from unittest import TestCase
from bod import Bod


class TestBod(TestCase):
    """Spouští testy funkcí pro práci s Body."""

    def test_vzdalenost_k_bodu_v_rovine(self):
        """Ověření výsledku vzdálenosti bodů v rovině."""
        self.assertEqual(
            Bod(0, 2).vzdalenost_k_bodu(Bod(0, 5)),
            3)
        self.assertAlmostEqual(
            Bod(0, 2.3).vzdalenost_k_bodu(Bod(0, 4.9)),
            2.6)

    def test_vzdalenost_k_bodu_ve_2d_prostoru(self):
        """Ověření výsledku vzdálenosti bodů ve 2D prostoru."""
        self.assertEqual(
            round(Bod(5, 2).vzdalenost_k_bodu(Bod(1, 6)), 3),
            5.657)

    def test_vzdalenost_k_bodu_s_minusovymi_souradnicemi_bodu(self):
        """Ověření výsledku vzdáleností bodů s mínusovými souřadnicemi."""
        self.assertEqual(
            round(Bod(3.23, -5).vzdalenost_k_bodu(Bod(-4, -3.5)), 3),
            7.384)
