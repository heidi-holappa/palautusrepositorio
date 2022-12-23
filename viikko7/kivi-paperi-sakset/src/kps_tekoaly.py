from tekoaly import Tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self):
        self.tekoaly = Tekoaly()

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
