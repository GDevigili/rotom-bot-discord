import discord as d
import private.app_data as my_app
from discord.ext.commands import Bot
# from model.CommandEvent import CommandEvent
from model.DaoNickname import DaoNickname

TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+", case_insensitive=True)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


# ----- # ----- # ----- # ----- # ----- # ----- #
# Compliment Functions


@bot.command(name="oi", aliases=["olá", "ola", "bom dia", "boa tarde", "boa noite"])
async def hi(msg):
    await msg.channel.send(f"Olá {msg.author.mention}")


# ----- # ----- # ----- # ----- # ----- # ----- #
# Nickname Functions


@bot.command(name="set-nick", aliases=["setnick", "set-nickname", "setnickname"])
async def set_nick(msg, game_nick=None):
    """
    Sets a new game nickname for the discord user
    """

    if game_nick:
        dao = DaoNickname()
        if dao.insert(msg.author.id, game_nick):
            await msg.channel.send(f"{str(str(msg.author.mention))} seu nick foi regizztrado com sucesso! \n"
                                   f"Ou será que eu deveria te chamar de **{game_nick}** agora? ")
        else:
            await msg.channel.send(error_msg("Unknow Error"))
    else:
        await msg.channel.send(
            f"Opzz, acho que não tem nenhum nick para eu registrar\n"
            f"Tente usar\n"
            f"```+setnick SeuNickAqui```")


@bot.command(name="nick", aliases=["n", "nickname"])
async def get_nick(msg, tagged_user=None):
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
            await msg.channel.send(f"```Nickname: {nickname[0][0]}```")
        else:
            await msg.channel.send(("Nick não encontrado"))
    else:
        await msg.channel.send("Parece que você não marcou ninguém, use "
                               "```+nick @SeuAmigoDoDiscord```"
                               "para ver se eu consigo achar o nick dele")


# @bot.command(name="discord-nick", aliases=["discordnick", "discord"])
# async def get_dicord_nick(msg, nickname):
#     pass


# ----- # ----- # ----- # ----- # ----- # ----- #
# Check-in Functions

# check_lst = []
#
#
# @bot.command(name="start-check-in", aliases=["start-checkin", "checkin-start", "check-in-start"])
# async def check_in_start():
#     global check_lst
#     check_lst = []
#
#
# @bot.command(name="check-in", aliases=["checkin"])
# async def check_in(msg):
#     check_lst.append(msg.author.id)
#     await msg.channel.send()
#
#
# @bot.command(name="check-in-list", aliases=["checkin-list", "check-list", "checklist", "clist"])
# async def check_in_list(msg):
#     return check_lst

def error_msg(error):
    return f"Parece que aconteceu o seguinte erro ao realizar esta ação:\n" \
           f"```diff" \
           f"- {error}" \
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
