import os
from dotenv import load_dotenv
import discord

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
@bot.event
async def on_message(message):
    print(f"recieved message in channel {message.channel} from {message.author}")

@bot.slash_command(name="hello", description="Say hello to scribe")
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(os.getenv('TOKEN'))
