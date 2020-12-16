from random import randint
from discord import User

class Elimination:
    def __init__(self, players:list):
        """
        The init function of the single elimination tournament
        :param players: a list with all the players of the tournament.
        """
        self.players = players.copy()
        self.active = players.copy()
        self.matches = self.generate_bracket()

    def get_players(self):
        """
        Returns the list with all players.
        """
        return self.players

    def get_active_players(self):
        """
        Returns a list with the players that are still in the tournament (active players).
        """
        return self.active

    def get_matches(self):
        """
        Returns a list with all the matches of the round.
        """
        return self.matches

    def matches_to_string(self, mention=False):
        """
        Returns a String with the matches.
        """
        matches_str = "As partidas da rodada são:\n"
        for match in self.matches:
            if type(match[0]) == User and mention:
                matches_str += f"{match[0].mention}"
            else:
                matches_str += f"{match[0]}"

            matches_str += " VS. "

            if type(match) == User and mention:
                matches_str += f"{match[1].mention}"
            else:
                matches_str += f"{match[1]}"
            matches_str += "\n"

        return matches_str

    def add_player(self, player):  # seria uma boa ideia limitar o tipo de entrada para o objeto correto
        """
        Adds a player in the players list
        :param player: The player who will be added
        """
        self.players.append(player)

    def drop_player(self, player):
        """
        Removes a player from the active players list
        :param player: The player who will be removed
        """
        self.active.remove(player)

    def generate_bracket(self):
        """
        Generates a single elimination bracket with the active players
        """
        aux_players = self.active.copy()
        power = 0
        while len(self.active) > 2**power:
            power += 1
        bracket_size = 2**power  # --> (1)
        print(bracket_size)

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

        matches = [[blue_side[i], red_side[i]] for i in range(len(blue_side))]  # -->(5)
        return matches

        # (1)--> Calculates the nearest power of two bigger than the number of players
        # (2)--> Selects half of the bracket size to be the "blue side" of the matches
        # (3)--> Selects the remaining players to be the "red side" of the matches
        # (4)--> Fills the red size with BYEs until the length of red_side is equal to half of the bracket size
        # (5)--> Pairs up the blue and red sides to make the matches


if __name__ == '__main__':
    players = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    e = Elimination(players)
    print(e.players)
    print(e.active)
    print(e.matches)
    print(e.matches_to_string())
