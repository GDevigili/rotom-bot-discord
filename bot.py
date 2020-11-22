import os

import discord as d
from dotenv import load_dotenv

import private.app_data as app

print(app.get_bot_token())

load_dotenv()
TOKEN = os.getenv(app.get_bot_token())

client = d.Client()

@client.event
async def on_ready():
    print(f'{client.user} has conected to Discord!')
    
client.run(TOKEN)