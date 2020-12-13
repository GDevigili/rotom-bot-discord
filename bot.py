import discord as d
import private.app_data as my_app
from discord.ext.commands import Bot
# from model.MessageEvent import
from model.CommandEvent import CommandEvent

TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+")


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command(name="oi", aliases=["olá", "ola"])
async def _hi(msg):
    await msg.channel.send(f"Olá {msg.author.mention}")

    
# --------------------------------
# class MyClient(d.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

bot.run(TOKEN)
