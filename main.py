import os
import fileinput
import time
from dotenv import load_dotenv
import discord
import date_finder

load_dotenv()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.id == 1127696067530604718:
        return
    print(f"received message in channel {message.channel} from {message.author.id}")


@bot.slash_command(name="view", description="See current daily note")
async def view(ctx):
    path = f"{os.getenv('FOLDER_PATH')}{date_finder.get_current_daily_note_filename()}"
    file = open(path, "r", encoding="UTF-8")
    file_content = file.read()
    file.close()
    embed = discord.Embed(
        title=f"Daily Note for {date_finder.get_current_date_yyyy_mm_dd()}"
    )
    # embed.add_field(name="contents", value=file_content)
    await ctx.respond(content=f"{file_content}", embed=embed)


@bot.slash_command(name="mtt", description="Message to Tomorrow")
async def mtt(ctx, content):
    path = f"{os.getenv('FOLDER_PATH')}{date_finder.get_current_daily_note_filename()}"
    file = open(path, "r", encoding="UTF-8")
    file_content = file.read()
    file.close()
    file = open(path, "a", encoding="UTF-8")
    if date_finder.get_message_to_tomorrow_title() not in file_content:
        file.write(date_finder.get_message_to_tomorrow_title())
        file.write(f"{content}")
    else:
        file.write(f", {content}")
    await ctx.respond(content=f"added ```{content}``` to mtt")
    await push(ctx=ctx, shouldRespond=False)


@bot.slash_command(name="imp", description="Important things")
async def imp(ctx, content):
    path = f"{os.getenv('FOLDER_PATH')}{date_finder.get_current_daily_note_filename()}"

    insert_at_header("## important things:", content, path)
    await ctx.respond(content=f"added ```{content}``` to imp")
    await push(ctx=ctx, shouldRespond=False)


@bot.slash_command(name="ttli", description="Important things")
async def ttli(ctx, content):
    path = f"{os.getenv('FOLDER_PATH')}{date_finder.get_current_daily_note_filename()}"

    insert_at_header("## things to look into:", content, path)
    await ctx.respond(content=f"added ```{content}``` to ttli")
    await push(ctx=ctx, shouldRespond=False)


@bot.slash_command(name="stf", description="Important things")
async def stf(ctx, content):
    path = f"{os.getenv('FOLDER_PATH')}{date_finder.get_current_daily_note_filename()}"

    insert_at_header("stuff that happened today:", content, path)
    await ctx.respond(content=f"added ```{content}``` to stf")
    await push(ctx=ctx, shouldRespond=False)


def insert_at_header(header, content, path):
    for line in fileinput.FileInput(path, inplace=True):
        content = f"- {content}"
        if header in line:
            line += content + os.linesep
        print(line, end="")


@bot.slash_command(name="push", description="does the git stuff for synchro")
async def push(ctx, should_respond=True):
    if should_respond:
        await ctx.respond(content="pushing changes to github")
    commit_msg = "update from scribe"
    os.chdir(os.getenv("FOLDER_PATH"))
    os.system("git pull")
    time.sleep(3)
    os.system("git add *")
    time.sleep(2)
    os.system(f'git commit -m "{commit_msg}"')
    time.sleep(2)
    os.system("git push")


bot.run(os.getenv("TOKEN"))
