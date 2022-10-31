import unittest
from statistic import Statistics
from player import Player
from statistic import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_lukija_palauttaa_listan_pelaajia(self):
        pelaajia = len(self.statistics._players)
        self.assertEqual(pelaajia, 5)

    def test_metodi_search_palauttaa_pelaajan_jos_pelaaja_loytyy(self):
        pelaaja = self.statistics.search("Semenko")
        maalit = None
        if pelaaja:
            maalit = pelaaja.goals
        self.assertEqual(maalit, 4)

    def test_metodi_search_palauttaa_tyhjan_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.statistics.search("Holappa")
        self.assertFalse(pelaaja)

    def test_metodi_team_palauttaa_oikean_maaran_pelaajia(self):
        edm = self.statistics.team("EDM")
        tanssijoita = len(edm)
        self.assertEqual(tanssijoita, 3)

    def test_lemieux_on_paras_pelaaja(self):
        paras = self.statistics.top(4)
        parhaan_nimi = paras[0].name
        self.assertEqual(parhaan_nimi, "Gretzky")

    def test_huonoin_pelaaja_on_semenko(self):
        paras = self.statistics.top(4)
        huonoimman_nimi = paras[4].name
        self.assertEqual(huonoimman_nimi, "Semenko")

    def test_eniten_assisteja_on_gretzky(self):
        eniten_assisteja = self.statistics.top(4, SortBy.ASSISTS)
        nimi = eniten_assisteja[0].name
        self.assertEqual(nimi, "Gretzky")

    def test_eniten_maaleja_on_lemieux(self):
        eniten_assisteja = self.statistics.top(4, SortBy.GOALS)
        nimi = eniten_assisteja[0].name
        self.assertEqual(nimi, "Lemieux")
