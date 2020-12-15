import discord as d
import private.app_data as my_app
from discord.ext.commands import Bot
# from model.CommandEvent import CommandEvent
from model.DaoNickname import DaoNickname
from random import randint

TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+", case_insensitive=True)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


# ----- # ----- # ----- # ----- # ----- # ----- #
# Compliment Functions


@bot.command(name="oi", aliases=["olá", "ola", "bom dia", "boa tarde", "boa noite"])
async def hi(ctx):
    await ctx.channel.send(f"Olá {ctx.author.mention}")


# ----- # ----- # ----- # ----- # ----- # ----- #
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
            await ctx.channel.send(error_msg("Unknown Error"))
    else:
        await ctx.channel.send(
            f"Opzz, acho que não tem nenhum nick para eu registrar\n"
            f"Tente usar\n"
            f"```+setnick SeuNickAqui```")


@bot.command(name="nick", aliases=["n", "nickname"])
async def get_nick(ctx, tagged_user=None):
    """
    Returns the nickname of the tagged discord user
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
    pass


# ----- # ----- # ----- # ----- # ----- # ----- #
# Check-in Functions

check_lst = []
check_in_status = False


@bot.command(name="start-check-in", aliases=["start-checkin", "checkin-start", "check-in-start"])
async def check_in_start(ctx):
    global check_lst
    check_lst = []
    global check_in_status
    check_in_status = True
    await ctx.channel.send("O check-in está aberto")


@bot.command(name="check-in", aliases=["checkin"])
async def check_in(ctx):
    if check_in_status:
        if ctx.author not in check_lst:
            check_lst.append(ctx.author)
            if ctx.author in check_lst:
                await ctx.channel.send("Check-in realizado com sucesso")
            else:
                await ctx.channel.send(error_msg("Check-in não realizado"))
        else:
            await ctx.channel.send("Check-in já realizado")
    else:
        await ctx.channel.send("O check-in não está aberto")


@bot.command(name="check-in-list", aliases=["checkin-list", "check-list", "checklist", "clist"])
async def check_in_list(ctx, mention=False):
    check_str = "Jogadores que realizaram o check-in:\n"
    for player in check_lst:
        if mention:
            check_str += f"> {player.mention}\n"
        else:
            check_str += f"> {player    }\n"
    await ctx.channel.send(check_str)


# ----- # ----- # ----- # ----- # ----- # ----- #
# Giveaway Functions
giveaway_list = []
giveaway_status = False

@bot.command(name="giveaway-start", aliases=["start-giveaway"])
async def giveaway_start(ctx, prize = None):
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
    giveaway_list.append(ctx.author)


@bot.command(name="giveaway")
async def giveaway(ctx, number=1):
    for i in range(number):
        global giveaway_list
        winner = giveaway_list[randint(0, len(giveaway_list) - 1)]
        await ctx.channel.send(f"Parabéns {winner}, você foi sorteado!")




def error_msg(error):
    return f"Parece que aconteceu o seguinte erro ao realizar esta ação:\n" \
           f"```" \
           f"{error}" \
           f"```\n" \
           f"Informe ao desenvolvedor para que ele possa ser resolvido"




# --------------------------------
# class MyClient(d.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
