# import discord as d
from discord.ext.commands import Bot
import re


def verify_message(bot: Bot, message):
    if message.content == str(bot.command_prefix + "bom dia"):
        return f"Bom dia {str(message.author)[:-5]}"

    if message.content == str(bot.command_prefix + "boa tarde"):
        return f"Boa tarde {str(message.author)[:-5]}"

    if message.content == str(bot.command_prefix + "boa noite"):
        return f"Boa noite {str(message.author)[:-5]}"

    if message.content == str(bot.command_prefix + "functions"):
        #modificar posteriormente para ele ler o .md com as funções
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

    # if len(re.findall(( bot.command_prefix + "nick"), message.content)):
    #     print("sup")


def set_nick(bot: Bot, message):
    pass


def get_nick(bot:Bot, message):
    pass