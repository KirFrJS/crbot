import discord
from discord.ext import commands
import os


crusty = commands.Bot(command_prefix='-')
crusty.remove_command('help')


  
token = os.environ.get('BOT_TOKEN')

crusty.run(str(token))
