"""Hlavní modul spuštějící program."""
from bod import Bod
from trojuhelnik import Trojuhelnik
import sys


def ziskej_souradnice_bodu(nazev):
    """
    Zažádá uživatele o zadání x a y souřadnic pro daný bod.

    :param string nazev: název bodu
    :return: Bod při zadání správných souřadnic, jinak None
    :rtype: Bod|None
    """
    try:
        coords = [float(i) for i in
                  input(f"Zadejte souřadnice bodu {nazev} oddělené mezerou: ")
                  .strip().replace(",", ".").split(" ")]
        if len(coords) == 2:
            print(f"Zadali jste bod {nazev}[{coords[0]};{coords[1]}]")
            return Bod(coords[0], coords[1])
        else:
            print("Nesprávný vstup, zadejte prosím dvě souřadnice.")
            return None
    except ValueError:
        print("Na vstupu je třeba zadat 2 numerické hodnoty.")
        return None


def spust_trojuhelnik():
    """Spustí program pro získání souřadnic bodů a zpracování trojúhelníku."""
    args = sys.argv
    pocet_args = len(args)
    if pocet_args == 1:  # spuštěno bez argumentů -> input prompty
        a = b = c = None
        while a is None:
            a = ziskej_souradnice_bodu("A")
            print()
        while b is None:
            b = ziskej_souradnice_bodu("B")
            print()
        while c is None:
            c = ziskej_souradnice_bodu("C")
            print()
    elif pocet_args == 7:  # spuštěno s argumenty z konzole
        try:
            a = Bod(float(args[1]), float(args[2]))
            b = Bod(float(args[3]), float(args[4]))
            c = Bod(float(args[5]), float(args[6]))
        except ValueError:
            print("CHYBA: nesprávný vstup, hodnoty musí být numerické.")
            sys.exit(1)
    else:  # spuštěno s argumenty, ale nesprávným počtem
        print(f"CHYBA: čekáváno 6 argumentů, obdrženo {pocet_args - 1}.")
        sys.exit(1)
    trojuhelnik = Trojuhelnik(a, b, c)
    trojuhelnik.vypis_vlastnosti()
    sys.exit(0)


if __name__ == '__main__':
    spust_trojuhelnik()
