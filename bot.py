import discord as d
import private.app_data as my_app
from discord.ext.commands import Bot
# from model.CommandEvent import CommandEvent
from model.DaoNickname import DaoNickname

TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+")


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command(name="oi", aliases=["olá", "ola", "bom dia", "boa tarde", "boa noite"])
async def _hi(msg):
    await msg.channel.send(f"Olá {msg.author.mention}")


@bot.command(name="set-nick", aliases=["setnick", "set-nickname", "setnickname"])
async def _set_nick(msg, game_nick=None):
    if game_nick:
        dao = DaoNickname()
        if dao.insert(msg.author, game_nick):
            await msg.channel.send(f"{str(str(msg.author.mention))} seu nick foi regizztrado com sucesso! \n"
                                   f"Ou será que eu deveria te chamar de **{game_nick}** agora? ")
        else:
            await msg.channel.send(error_msg("Unknow Error"))
    else:
        await msg.channel.send(f"Opzz, acho que não tem nenhum nick para eu registrar\nTente usar\n```+nick SeuNick```")


@bot.command(name="nick", aliases=["n", "nickname"])
async def get_nick(msg):
    dao = DaoNickname()
    nickname = dao.select_nickname(msg.author)
    if nickname:
        await msg.channel.send( f"```Nickname: {nickname}```")
    else:
        await error_msg("Nick não encontrado")


def error_msg(error):
    return f"Parece que aconteceu o seguinte erro ao realizar esta ação:\n" \
           f"```{error}```\n" \
           f"Informe ao desenvolvedor para que ele possa ser resolvido"
# --------------------------------
# class MyClient(d.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
