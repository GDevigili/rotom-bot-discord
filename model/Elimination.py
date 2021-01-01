from random import randint
from discord.member import Member
from model.Match import Match


class Elimination:
    def __init__(self, players: list):
        """
        The init function of the single elimination tournament
        :param players: a list with all the players of the tournament.
        """
        self.players = players.copy()
        self.active = players.copy()
        self.generate_bracket()
        self.matches = []

# ----------------------------------------------------------------------------------------------------------------------
# Getters

    def get_players(self):
        """
        Return the list with all players.
        """
        return self.players

    def get_active_players(self):
        """
        Return a list with the players that are still in the tournament (active players).
        """
        return self.active

    def get_matches(self):
        """
        Return a list with all the matches of the round.
        """
        return self.matches

# ----------------------------------------------------------------------------------------------------------------------
# Aesthetic functions

    def matches_to_string(self):
        """
        Return a String with the matches.
        """
        matches_str = "As partidas da rodada são:\n"
        cont = 0
        for match in self.matches:
            cont += 1
            matches_str += f"> ID: {cont} | {match.to_string()} \n"
        return matches_str

# ----------------------------------------------------------------------------------------------------------------------
# Player Management

    def add_player(self, player: Member):
        """
        Add a player in the players list
        :param player: The player who will be added
        """
        self.active.append(player)

    def drop_player(self, player):
        """
        Drop a player from the tournament
        :param player: The player who will be removed
        """
        self.players.remove(player)

    def eliminate(self, player):
        """
        Eliminate a player from de tournament
        :param player: The player who will be removed
        """
        self.active.remove(player)

# ----------------------------------------------------------------------------------------------------------------------
# Bracket Management

    def generate_bracket(self):
        """
        Generate a single elimination bracket with the active players
        """
        aux_players = self.active.copy()
        power = 0
        while len(self.active) > 2**power:
            power += 1
        bracket_size = 2**power  # --> (1)

        blue_side = []
        for i in range(int(bracket_size/2)):
            p = aux_players.pop(randint(0, len(aux_players) - 1))  # --> (2)
            blue_side.append(p)

        red_side = []
        for i in range(len(aux_players)):
            p = aux_players.pop(randint(0, len(aux_players) - 1))  # -->(3)
            red_side.append(p)

        for i in range(int(bracket_size/2) - len(red_side)):  # -->(4)
            red_side.append("BYE")

        matches = [Match(blue_side[i], red_side[i]) for i in range(len(blue_side))]  # -->(5)

        self.matches = matches

        # (1)--> Calculates the nearest power of two bigger than the number of players
        # (2)--> Selects half of the bracket size to be the "blue side" of the matches
        # (3)--> Selects the remaining players to be the "red side" of the matches
        # (4)--> Fills the red size with BYEs until the length of red_side is equal to half of the bracket size
        # (5)--> Pairs up the blue and red sides to make the matches

    def locate_match(self, player):
        """
        Locates the match which has the param player
        :param player: the player who is in the wanted match
        :return: the match which has the specified player
        """
        for match in self.matches:
            if player in match.players:
                return match

# ----------------------------------------------------------------------------------------------------------------------
# Tests


if __name__ == '__main__':
    players = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    e = Elimination(players)
    print(e.matches_to_string())

    e.eliminate('p3')
    e.eliminate('p4')
    print(e.active)
    e.generate_bracket()
    print(e.matches_to_string())

    e.eliminate('p1')
    e.eliminate('p2')
    print(e.active)
    e.generate_bracket()
    print(e.matches_to_string())
