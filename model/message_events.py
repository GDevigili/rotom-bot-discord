# import discord as d
from discord.ext.commands import Bot
import re

def verify_message(bot: Bot, message):
    if message.content == str((bot.command_prefix + "bom dia")):
        return f'Bom dia {message.author}'
    if len(re.findall((bot.command_prefix + "nick"), message.content)):


def set_nick(bot: Bot, message):
    pass

def get_nick(bot:Bot, message):
    pass