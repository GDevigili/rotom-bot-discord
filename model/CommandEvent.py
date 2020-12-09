# import discord as d
from discord.ext.commands import Bot
import re


class CommandEvent:
    def __init__(self, bot: Bot, message):
        self.bot = bot
        self.message = message
        aux_lst = re.split(str(message.content), " ")
        self.command = aux_lst[0]
        self.args = aux_lst[1:]

    def verify_message(self):
        if self.command in self.greet_list(self.bot):
            return self.greet()

        if self.command == "+set-nick":  # vai precisar usar o DAO para isso
            return self.under_construction()

        if self.command == "+nick":
            return self.under_construction()  # preciso registrar isso no banco agr

        # if len(re.findall(( bot.command_prefix + "nick"), message.content)):
        #     print("sup")

    @staticmethod
    def under_construction(self):
        return "Oopzz! Parece que esta função ainda ezztá sendo dezzenvolvida bzz"

    def greet(self):
        return str(self.message.content)[1:] + " " + str(str(self.message.author)[:-5])

    def greet_list(self):
        greet_list = ["bom dia",
                     "boa tarde",
                     "boa noite",
                     "oi"]
        return [str(self.bot.command_prefix) + greet for greet in greet_list]

    def set_nick(self):
        pass

    def get_nick(self):
        pass

