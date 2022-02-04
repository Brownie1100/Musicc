import discord
from discord.ext import commands
import mooseic

cogs=[mooseic]

client =commands.Bot(command_prefix="-", intents=discord.Intents.all(), case_insensitive=True)
for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTA0MzI2NjgxNzE0NjU1MjQy.YX552g.bmql6FOLh0AcfBCJm3KNSWvAHKk")