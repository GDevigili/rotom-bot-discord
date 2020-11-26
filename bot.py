import discord as d
import private.app_data as my_app

client = d.Client()

TOKEN = my_app.get_bot_token()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return message.channel.send('Adm corno!')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
client.run(TOKEN)