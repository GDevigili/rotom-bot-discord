from discord.member import Member


class Match:
    def __init__(self, p0, p1):
        self.players = [p0, p1]
        self.winner = None

    def set_player(self, player, id):
        self.players[id] = player

    def set_winner(self, player):
        self.winner = player

    def __str__(self, mention):
        if type(self.players[0]) == Member and mention:
            match_str = f"{self.players[0].mention}"
        else:
            match_str = f"{self.players[0]}"

        match_str += " VS. "

        if type(self.players[1]) == Member and mention:
            match_str += f"{self.players[1].mention}"
        else:
            match_str += f"{self.players[1]}"

        return match_str
