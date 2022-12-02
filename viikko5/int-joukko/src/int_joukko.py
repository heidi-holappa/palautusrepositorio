class IntJoukko:
    def __init__(self, turhamuuttuja=None, turhamuuttuja2=None):
        self.lukujono = []

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if n in self.lukujono:
            return False
        self.lukujono.append(n)

    def poista(self, n):
        if n not in self.lukujono:
            return False
        self.lukujono.remove(n)
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        alkiot = a.to_int_list() + b.to_int_list()

        uusi_joukko.lisaa_alkiot(uusi_joukko, alkiot)

        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        alkiot = [alkio for alkio in a.to_int_list()
                  if alkio in b.to_int_list()]

        uusi_joukko.lisaa_alkiot(uusi_joukko, alkiot)

        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()

        alkiot = [alkio for alkio in a.to_int_list()
                  if alkio not in b.to_int_list()]

        uusi_joukko.lisaa_alkiot(uusi_joukko, alkiot)
        return uusi_joukko

    @staticmethod
    def lisaa_alkiot(joukko, alkiot):
        for alkio in alkiot:
            joukko.lisaa(alkio)

    def __str__(self):
        return f"\u007b{', '.join(map(str, self.lukujono))}\u007d"
