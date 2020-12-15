from random import randint


class Elimination:
    def __init__(self, players: list):
        self.players = players
        self.active = players
        self.matches = self.generate_bracket()

    def get_players(self):
        return self.players

    def get_active_players(self):
        return self.active

    def get_matches(self):
        return self.matches

    def add_player(self, player):
        self._players.append(player)

    def drop_player(self, player):
        self._active.remove(player)

    def generate_bracket(self):
        power = 0
        while len(self.players) > 2**power:
            power += 1
        bracket_size = 2**power
        blue_side = []
        aux_players = self.players
        for i in range(int(bracket_size/2)):
            p = aux_players.pop(randint(0, len(aux_players) - 1))
            blue_side.append(p)
        red_side = []
        for i in range(len(aux_players)):
            p = aux_players.pop(randint(0, len(aux_players) - 1))
            red_side.append(p)
        for i in range(int(bracket_size/2) - len(red_side)):
            red_side.append("BYE")
        matches = [blue_side[i] + " X " + red_side[i] for i in range(len(blue_side))]
        return matches

if __name__ == '__main__':
    players = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    e = Elimination(players)
    # print(e.players)
    print(e.generate_bracket())
