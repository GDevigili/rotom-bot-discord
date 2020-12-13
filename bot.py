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


@bot.command(name="set-nick", aliases=["setnick"])
async def _set_nick(msg, game_nick=None):
    if game_nick:
        dao = DaoNickname()
        if dao.insert(msg.author, game_nick):
            await msg.channel.send(f"{str(str(msg.author.mention))} seu nick foi regizztrado com sucesso :)! \n"
                                   f"Ou será que eu deveria te chamar de **{game_nick}** agora? ")
        else:
            await msg.channel.send(f"Aconteceu o seguinte erro:\n```{self.error_message()}```\nPor favor, informe ")
    else:
        await msg.channel.send(f"Opzz, acho que não tem nenhum nick para eu registrar\nTente usar\n```+nick SeuNick```")


# --------------------------------
# class MyClient(d.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
