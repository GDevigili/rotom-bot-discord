
class Elimination:
    def __init__(self, players: list):
        self.players = []
        self.set_players(players)
        self.active = players

    def set_players(self, players_list: list):
        power = 0
        while len(players_list) > 2**power:
        while len(players_list) > 2**power:
            power += 1

        for i in range(2**power - len(players_list)):
            players_list.append("BYE")
            self.players = players_list

    def add_player(self, player):
        self._players.append(player)

    def drop_player(self, player):
        self._players.remove(player)


if __name__ == '__main__':
    players = ['p1', 'p2', 'p3', 'p4', 'p5']
    e = Elimination(players)
    print(e.players)