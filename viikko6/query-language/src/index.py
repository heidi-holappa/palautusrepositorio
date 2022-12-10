from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print(40*"-")
    print("PRINTING TEST 1: (PLAYERS WITH ATLEAST 5 GOALS AND 5 ASSISTS")
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print(40*"-")
    print("PRINTING TEST 2: (SHOULD CONTAIN ALL PLAYERS WITH ZERO GOALS)")
    matcher2 = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher2):
        print(player)

    print(40*"-")
    print("PRINTING TEST 3: (SHOULD MATCH TEST 2")
    matcher3 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher3):
        print(player)

    print(40*"-")
    print("PRINTING TEST 4: ALL (SHOULD RETURN TRUE")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all) == len(stats._players))

    print(40*"-")
    print("PRINTING TEST 5: OR")
    matcher5 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher5):
        print(player)

    print(40*"-")
    print("PRINTING TEST 6: OR")
    matcher6 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher6):
        print(player)


if __name__ == "__main__":
    main()
