from playerreader import PlayerReader
from playerstats import PlayerStats


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    # response = requests.get(url).json()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Printing players with nationality: FIN")
    print(f"{'Name':20}{'Team':6}{'Goals + assists':20}")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
