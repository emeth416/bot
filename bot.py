import discord
from discord.ext import commands


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(999362544978382898)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(999362544978382898)
    await channel.send(f'{member} leave!')

bot.run('OTk4OTk0Njk0NzQ0ODUwNDMy.GtX6j-.D1fID9KGWlUxaHgVy7-77xOy_tDWXmBdnMHD3A')
