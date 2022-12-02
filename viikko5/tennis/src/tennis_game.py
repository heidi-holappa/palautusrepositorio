class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.points = {
            player1_name: 0,
            player2_name: 0
        }
        self.tennis_dictionary = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

    def won_point(self, player_name):
        self.points[player_name] += 1

    def get_score(self):
        score = ""
        current_score = (self.points[self.player1], self.points[self.player2])

        if current_score[0] == current_score[1]:
            if current_score[0] > 3:
                score = "Deuce"
            else:
                score = self.tennis_dictionary[current_score[0]] + "-All"

        elif max(current_score) >= 4:
            difference_in_points = abs(current_score[0] - current_score[1])

            if difference_in_points == 1:
                if current_score[0] > current_score[1]:
                    score = "Advantage player1"
                else:
                    score = "Advantage player2"
            else:
                if current_score[0] > current_score[1]:
                    score = "Win for player1"
                else:
                    score = "Win for player2"
        else:
            score = self.tennis_dictionary[current_score[0]] + \
                "-" + self.tennis_dictionary[current_score[1]]

        return score
