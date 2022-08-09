import discord
from discord import *
from discord.ext import commands

token=""
client = discord.Client()

@client.event
async def on_ready():
    print("embed 출력을 시작합니다. 원하는 채널에 명령어를 입력하세요.")

@client.event
async def on_message(message):
  if message.author.bot:
    return None

  if message.content == ";embed":
    embed=discord.Embed(title="SCT 주요 사항들(21.10.10)", color=0x00d9ff)
    embed.add_field(name="", value="", inline=False)
    embed.set_footer(text="With SCT")
    await message.channel.send(embed=embed)

client.run(token)