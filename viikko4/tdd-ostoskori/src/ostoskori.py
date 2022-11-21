from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self.tuotteet = {}
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        maara = 0
        for avain, tuote in self.tuotteet.items():
            maara += tuote.lukumaara()
        return maara

    def hinta(self):
        kokonaishinta = 0
        for tuote in self.tuotteet.values():
            kokonaishinta += tuote.hinta()
        return kokonaishinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if not lisattava.nimi in self.tuotteet:
            self.tuotteet[lisattava.nimi] = Ostos(lisattava)
        else:
            self.tuotteet[lisattava.nimi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
