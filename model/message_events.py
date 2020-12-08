# import discord as d
from discord.ext.commands import Bot
import re


def verify_message(bot: Bot, message):
    if str(message.content) in greet_list(bot):
        return greet(message)

    if message.content == str(bot.command_prefix + "functions"):
        # modificar posteriormente para ele ler o .md com as funções
        return """
        Aqui ezztá tudo o que eu consigo fazer bzz:
        **Funções:**
        +bom dia/boa tarde/boa noite: comprimenta o usuário
        -------------------------
        **Em desenvolvimento:**
        +nick <username>: retorna o nickname do usuário no jogo
        +set-nick <nickname>: seta o nickname do usuário no jogo para o texto informado 
        -------------------------
        **Próximas Funções:**
        +giveaway <text>: sorteia um usuário e marca ele 
        +create-tour <type> <text>: cria um torneio
        +check-in: faz o check-in do usuário no torneio
        +gen-elimination: gera um torneio do tipo *eliminação simples* com os usuários que fizeram check-in
        """

    if str(message.content)[:9] == "+set-nick":  # vai precisar usar o DAO para isso
        pass

    if str(message.content)[:5] == "+nick":
        pass  # preciso registrar isso no banco agr

    # if len(re.findall(( bot.command_prefix + "nick"), message.content)):
    #     print("sup")


def greet(message):
    return str(message.content)[1:] + " " + str(str(message.author)[:-5])


def greet_list(bot: Bot):
    greet_list = ["bom dia",
                 "boa tarde",
                 "boa noite",
                 "oi"]
    return [str(bot.command_prefix) + greet for greet in greet_list]


def set_nick(bot: Bot, message):
    pass


def get_nick(bot: Bot, message):
    pass
