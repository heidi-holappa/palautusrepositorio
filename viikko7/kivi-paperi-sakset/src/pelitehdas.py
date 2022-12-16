from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja


class Pelitehdas:

    def __init__(self):
        pass

    @staticmethod
    def luo_pelaaja_vs_pelaaja_peli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_pelaaja_vs_tekoaly():
        return KPSTekoaly()

    @staticmethod
    def luo_pelaaja_vs_parempi_tekoaly():
        return KPSParempiTekoaly()
