import discord as d
import private.app_data as my_app
from discord.ext.commands import Bot
from model.message_events import verify_message

TOKEN = my_app.get_bot_token()
bot = Bot(command_prefix="+")

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if verify_message(bot, message):
        await message.channel.send(verify_message(bot, message))

# --------------------------------

# class MyClient(d.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

bot.run(TOKEN)