from random import randint
from discord.member import Member
from model.Match import Match


class Swiss:
    def __init__(self, players:list, rounds:int = 0):
        self.players = players
        if not rounds:
            self.rounds = len(players) - 1
        else:
            self.rounds = rounds