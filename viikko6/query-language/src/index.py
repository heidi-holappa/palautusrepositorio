from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from querybuilder import QueryBuilder


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

    # TASK 4:
    print("\n")
    print(' TASK 4 '.center(80, '-'))
    print(' TEST 7: QUERYSTACK ALL '.center(80, '-'))

    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder(stats)
    matcher7 = query.build()
    print(len(stats.matches(matcher7)))

    print("\n")
    print(' TEST 8: QUERYSTACK NYR '.center(80, '-'))

    query2 = QueryBuilder(stats)
    matcher8 = (
        query2
        .playsIn("NYR")
        .build()
    )

    for player in stats.matches(matcher8):
        print(player)

    print("\n")
    print(' TEST 9: QUERYSTACK OR 10<=GOALS<20'.center(80, '-'))

    query3 = QueryBuilder(stats)
    matcher9 = (
        query3
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
    )

    for player in stats.matches(matcher9):
        print(player)
    print("\n")
    print(' TASK 5 '.center(80, '-'))
    print(' TEST 10: QUERYSTACK OR '.center(80, '-'))
    matcher10 = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher10):
        print(player)


if __name__ == "__main__":
    main()
