import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
     print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")



client.run(os.environ.get("TOKEN"))
