class LeaderBoard:
    def __init__(self):
        self.scoreboard = {}

    def average(self, player_list):
        if player_list == []:
            return 0
        else:
            return sum(player_list) / len(player_list)

    def add_score(self, player_id, score):
        if player_id in self.scoreboard:
            self.scoreboard[player_id].append(score)
            return self.average(self.scoreboard[player_id])
        else:
            self.scoreboard[player_id] = [float(score)]
            return float(score)

    def top(self, max):
        top_players = []

        for player in self.scoreboard:
            top_players.append((player, self.average(self.scoreboard[player])))
        player_list = sorted(top_players, key=lambda x: x[1], reverse=True)[:max]
        return [player[0] for player in player_list]

    def reset(self, player_id):
        self.scoreboard[player_id] = []

leader_board = LeaderBoard()

print(leader_board.add_score(1, 50))
print(leader_board.add_score(2, 80))
print(leader_board.add_score(2, 70))
print(leader_board.add_score(4, 60))
print(leader_board.add_score(6, 90))
print(leader_board.add_score(3, 85))
print(leader_board.top(3))
print(leader_board.top(2))
print(leader_board.top(1))
leader_board.reset(3)
print(leader_board.top(3))
print(leader_board.add_score(3, 90))
print(leader_board.add_score(3, 85))
