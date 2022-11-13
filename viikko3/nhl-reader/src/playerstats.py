from player import Player


class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        playerdata = self.reader.get_players()
        players = []

        for player_dict in playerdata:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'],
            )
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda p: p.goals + p.assists, reverse=True)
        return players
