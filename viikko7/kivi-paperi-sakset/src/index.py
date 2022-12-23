from pelitehdas import Pelitehdas


def main():
    pelimuodot = {
        "a": Pelitehdas().luo_pelaaja_vs_pelaaja_peli,
        "b": Pelitehdas().luo_pelaaja_vs_tekoaly,
        "c": Pelitehdas().luo_pelaaja_vs_parempi_tekoaly
    }
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if pelimuodot.get(vastaus):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            pelimuoto = pelimuodot[vastaus]
            pelimuoto().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
