from discord.member import Member


class Match:
    def __init__(self, p0, p1):
        self.players = [p0, p1]
        self.winner = None

    def set_player(self, player, id):
        self.players[id] = player

    def set_winner(self, player):
        self.winner = player
