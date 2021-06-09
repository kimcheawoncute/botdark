import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os

bot = commands.Bot(command_prefix='중2야 ')

@bot.event
async def on_ready():
    print("Online")
    message = [f"{round(bot.latency*1000)}ms핑 이네", "현재 봇 테스트..."]
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(3)
    

@bot.event
async def on_message(message):
    if message.content.startswith("중2 멍청이"):
        await message.channel.send("ㅇ? 너 시험지 딱대")
    await bot.process_commands(message)

    if message.content.startswith("중2 뭐해"):
        await message.channel.send("아무것도 안하는중인데")
    await bot.process_commands(message)

    if message.content.startswith("중2 짖어!"):
        await message.channel.send("으르르.. 왈왈!")
    await bot.process_commands(message)

    if message.content.startswith("중2 언제 태어남?"):
        await message.channel.send("2021년 6월 8일 6시 52분에 깨어남")
    await bot.process_commands(message)

    if message.content.startswith("중2 어디살아?"):
        await message.channel.send("ㅇ? 니 알빠임?")
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")
    
access_token = os.environ["BOT_TOKEN"]

bot.run(access_token)
