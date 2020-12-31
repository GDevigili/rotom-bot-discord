# Discord API imports
# from itertools import chain

import discord as d
from discord.ext.commands import Bot
from discord.ext import commands

# Project imports
import private.app_data as my_app
from model.DaoNickname import DaoNickname
from model.Elimination import Elimination

# Other imports
from random import randint


TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+", case_insensitive=True)

admin_role = 'Kahuna'


@bot.event
async def on_ready():
    """
    Prints on the console when the bot connects to Discord
    """
    print(f'Bot connected as {bot.user}')

"""
@bot.event
async def on_message(message):
    if str(message.author.id) == "635629811993411594" or "<@!635629811993411594>" in message.content:
        await message.add_reaction("<:CorvoBan:782690759522123816>")
"""

# ----------------------------------------------------------------------------------------------------------------------
# Help Function


# @bot.command(name="help", aliases=["h", "ajuda"])
# async def help(ctx, command=None):
#     command_help_list = ["check-in"]
#     if command is None:
#         await ctx.channel.send("Informe o comando do qual você quer ajuda")
#         return 0
#     if command == "report":
#         pass

# ----------------------------------------------------------------------------------------------------------------------
# Compliment Functions


@bot.command(name="oi", aliases=["olá", "ola", "bom dia", "boa tarde", "boa noite"])
async def hi(ctx):
    """
    The bot compliments the user that used the command
    """
    await ctx.channel.send(f"Olá {ctx.author.mention}")


# ----------------------------------------------------------------------------------------------------------------------
# Nickname Functions


@bot.command(name="set-nick", aliases=["setnick", "set-nickname", "setnickname"])
async def set_nick(ctx, game_nick=None):
    """
    Sets a new game nickname for the discord user
    """

    if game_nick:
        dao = DaoNickname()
        if dao.insert(ctx.author.id, game_nick):
            await ctx.channel.send(f"{str(str(ctx.author.mention))} seu nick foi regizztrado com sucesso! \n"
                                   f"Ou será que eu deveria te chamar de **{game_nick}** agora? ")
        else:
            await ctx.channel.send(error_msg("Nickname não registrado"))
    else:
        await ctx.channel.send(
            f"Opzz, acho que não tem nenhum nick para eu registrar\n"
            f"Tente usar\n"
            f"```+setnick SeuNickAqui```")


@bot.command(name="nick", aliases=["n", "nickname"])
async def get_nick(ctx, tagged_user=None):
    """
    Send a message with the game nickname of the tagged discord user
    """
    if tagged_user:
        print(tagged_user)
        aux = [char for char in tagged_user if char.isdigit()]
        print(aux)
        tagged_user = "".join(map(str, aux))
        print(tagged_user)
        dao = DaoNickname()
        nickname = dao.select_nickname(tagged_user)
        if nickname:
            await ctx.channel.send(f"```Nickname: {nickname[0][0]}```")
        else:
            await ctx.channel.send("Nick não encontrado")
    else:
        await ctx.channel.send("Parece que você não marcou ninguém, use "
                               "```+nick @SeuAmigoDoDiscord```"
                               "para ver se eu consigo achar o nick dele")


@bot.command(name="discord-nick", aliases=["discordnick", "discord"])
async def get_discord_nick(ctx, nickname):
    """
    Send a message tagging the discord user that has the given game nickname.
    """
    pass


# ----------------------------------------------------------------------------------------------------------------------
# Check-in Functions

check_lst = []
check_in_status = False


@bot.command(name="start-check-in", aliases=["start-checkin", "checkin-start", "check-in-start"])
@commands.has_any_role(admin_role)
async def check_in_start(ctx):
    f"""
    Starts the check-in of a tournament.
    This function allows the users to use the {bot.command_prefix}check-in function.
    """
    global check_lst
    global check_in_status
    check_lst = []
    check_in_status = True
    await ctx.channel.send(f"O check-in está aberto!. "
                           f"Use o comando `{bot.command_prefix}check-in` para participar do torneio")


@bot.command(name="check-in", aliases=["checkin"])
async def check_in(ctx):
    """
    Add the author of the message to the check-in list.
    """
    if check_in_status:
        if ctx.author not in check_lst:
            check_lst.append(ctx.author)
            if ctx.author in check_lst:
                await ctx.channel.send(f"{ctx.author.mention}, seu check-in foi realizado com sucesso")
            else:
                await ctx.channel.send(error_msg("Check-in não realizado"))
        else:
            await ctx.channel.send(f"{ctx.author.mention}, seu check-in já foi realizado")
    else:
        await ctx.channel.send("O check-in não está aberto")


@bot.command(name="check-in-list", aliases=["checkin-list", "check-list", "checklist", "clist"])
async def check_in_list(ctx, mention=False):
    """
    Send all the registered users as a message.
    :param ctx: param automatically passed by the discord
    :param mention: makes the bot mention the users that made the check-in.
                    If the param is no passed, the bot will not mention the registered users.
    """
    check_str = "Jogadores que realizaram o check-in:\n"
    for player in check_lst:
        if mention:
            check_str += f"> {player.mention}\n"
        else:
            check_str += f"> {player}\n"
    await ctx.channel.send(check_str)

# ----------------------------------------------------------------------------------------------------------------------
# Tournament Functions

tournament = Elimination([])


@bot.command(name="start-tournament", aliases=["tournament-start"])
@commands.has_any_role(admin_role)
async def start_tournament(ctx, type:str="elimination"):
    global check_lst
    if type.lower() == "elimination":
        global tournament
        tournament = Elimination(check_lst)
        await ctx.channel.send(tournament.matches_to_string())


@bot.command(name="report")
async def report_score(ctx, result:str=None):
    if str(result).lower() not in ["win", "loss"]:
        await ctx.channel.send(f"Parece que você usou errado este comando.\n"
                               f"Tente usar `{bot.command_prefix}report win` se você venceu ou "
                               f"`{bot.command_prefix}report loss` se você perdeu")
    else:
        global tournament
        if str(result).lower() == "loss":
            tournament.eliminate(ctx.author)
        else:
            match = tournament.locate_match(player=ctx.author)
            if ctx.author == match[0]:
                tournament.eliminate(match[0])
            else:
                tournament.eliminate(match[1])

# ----------------------------------------------------------------------------------------------------------------------
# Giveaway Functions
giveaway_list = []
giveaway_status = False
giveaway_channel = ''


@bot.command(name="giveaway-start", aliases=["start-giveaway"])
async def giveaway_start(ctx, prize=None):
    if prize:
        await ctx.channel.send(f"""
É hora do Roto Loto :)        
e vamos sortear um {prize}!!!
para participar, digite `+me` aqui em baixo para entrar na lista do sorteio
        """)
        global giveaway_status
        giveaway_status = True


@bot.command(name="me")
async def giveaway_register(ctx):
    global giveaway_list
    if ctx.author not in giveaway_list:
        giveaway_list.append(ctx.author)
        await ctx.channel.send(f"{ctx.author.mention} você foi registrado com sucesso! \nBoa sorte!")
    else:
        await ctx.channel.send(f"Parece que você já está registrado. Boa sorte!")


@bot.command(name="giveaway")
async def giveaway(ctx, number=1):
    for i in range(number):
        global giveaway_list
        winner = giveaway_list[randint(0, len(giveaway_list) - 1)]
        await ctx.channel.send(f"Parabéns {winner.mention}, você foi sorteado, "
                               f"fale com o criador do sorteio para resgatar o prêmio!")
        global giveaway_status
        giveaway_status = False
        giveaway_list = []


# ----------------------------------------------------------------------------------------------------------------------

def error_msg(error):
    return f"Parece que aconteceu o seguinte erro ao realizar esta ação:\n" \
           f"```" \
           f"{error}" \
           f"```\n" \
           f"Informe ao desenvolvedor para que ele possa ser resolvido"

bot.run(TOKEN)
