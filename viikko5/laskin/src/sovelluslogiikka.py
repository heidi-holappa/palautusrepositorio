class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.kumoa = self.kumoa

    def kumoa(self):
        pass


class Summa:

    def __init__(self, sovelluslogiikka: Sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
        self.edellinen = 0

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos += int(self.io())
        self.sovelluslogiikka.kumoa = self.kumoa

    def kumoa(self):
        self.sovelluslogiikka.tulos = self.edellinen


class Erotus:

    def __init__(self, sovelluslogiikka, io):
        self.edellinen = 0
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos -= int(self.io())
        self.sovelluslogiikka.kumoa = self.kumoa

    def kumoa(self):
        self.sovelluslogiikka.tulos = self.edellinen


class Nollaus:

    def __init__(self, sovelluslogiikka, io):
        self.edellinen = 0
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos = 0
        self.sovelluslogiikka.kumoa = self.kumoa

    def kumoa(self):
        self.sovelluslogiikka.tulos = self.edellinen


class Kumoa:

    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io

    def suorita(self):
        self.sovelluslogiikka.kumoa()
