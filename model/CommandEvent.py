# import discord as d
from discord.ext.commands import Bot
from model.DaoNickname import DaoNickname


class CommandEvent:
    def __init__(self, bot: Bot, message):
        self.bot = bot
        self.message = message
        self.aux_lst = message.content.split(" ")
        self.command = self.aux_lst[0]
        self.args = self.aux_lst[1:]

    # Main
    def verify_message(self):
        if self.command in self.greet_list():
            return self.greet()

        if self.command == str(self.bot.command_prefix + "set-nick"):
            return self.set_nick(self.aux_lst[1])

        if self.command == str(self.bot.command_prefix + "nick"):
            return self.get_nick()

    # Greeting Functions
    def greet(self):
        return str(self.message.content)[1:] + " " + str(str(self.message.author)[:-5])

    def greet_list(self):
        greet_list = ["bom-dia",
                      "boa-tarde",
                      "boa-noite",
                      "oi"]
        return [str(self.bot.command_prefix) + greet for greet in greet_list]

    # Nickname Functions
    def set_nick(self, game_nick):
        dao = DaoNickname()
        if dao.insert(self.message.author, game_nick):
            return (f"{str(str(self.message.author)[:-5])} seu nick foi regizztrado com sucesso :)! \n"
                   f"Ou será que eu deveria te chamar de **{game_nick}** agora? ")

        else:
            return self.error_message()

    def get_nick(self):
        dao = DaoNickname()
        nickname = dao.select_nickname(self.message.author)
        print(nickname)
        if nickname:
            return f"```Nickname: {nickname}```"
        else:
            return self.error_message()

    @staticmethod
    def under_construction(self):
        return "Oopzz! Parece que esta função ainda ezztá sendo dezzenvolvida bzz"

    def error_message(self):
        return ("Oopz, parece que *bip* aconteceu algum *bop erro ao realizar ezzta ação!\n"
                    "Tente de novo ou reporte o erro ao desenvolvedor")