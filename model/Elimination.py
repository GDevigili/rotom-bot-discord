from random import randint

class Elimination:
    def __init__(self, players: list):
        self.players = players
        self.active = players

    # def set_players(self, players_list: list):
    #     power = 0
    #     while len(players_list) > 2**power:
    #     while len(players_list) > 2**power:
    #         power += 1
    #
    #     for i in range(2**power - len(players_list)):
    #         players_list.append("BYE")
    #         self.players = players_list

    def add_player(self, player):
        self._players.append(player)

    def drop_player(self, player):
        self._players.remove(player)

    def generate_bracket(self):
        power = 0
        while len(self.players) > 2**power:
            power += 1
        bracket_size = 2**power
        blue_side = []
        aux_players = self.players
        for i in range(int(bracket_size/2)):
            print(len(aux_players))
            p = aux_players.pop(randint(0, len(aux_players)))
            blue_side.append(p)
        return blue_side



if __name__ == '__main__':
    players = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    e = Elimination(players)
    # print(e.players)
    print(e.generate_bracket())
