import os
import time
import traceback
import datetime
import requests
from discord.ext import commands
from script import common
from script import speedrun
import random

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def schedule(ctx):
    await ctx.send('https://horaro.org/rtaij/rtaij2020')

@bot.command()
async def rij(ctx):
    await ctx.send('https://www.twitch.tv/rtainjapan')

@bot.command()
async def muteki(ctx):
    await ctx.send('https://mutekijikan.stores.jp/')    

@bot.command()
async def redbull(ctx):
    await ctx.send('https://www.redbull.com/')

@bot.command()
async def lagoon(ctx):
    randnum = random.randrange(14)
    if randnum == 0:
        await ctx.send('そんなCommand…返事はPASSさ…')
    elif randnum == 1:
        await ctx.send('そうさ、俺は…『RTABot』…誰かがそう教えてくれた…')
    elif randnum == 2:
        await ctx.send('返事をしろだと…冗談じゃねぇ…')
    elif randnum == 3:
        await ctx.send('『わかんねえだろうなあ…』')
    elif randnum == 4:
        await ctx.send('Driving Yokohama FOREVER!!')
    elif randnum == 5:
        await ctx.send('【声】が…アイツが俺を奪ってる…')
    elif randnum == 6:
        await ctx.send('RTABotさ…ごま塩程度に覚えておいてくれ…')
    elif randnum == 7:
        await ctx.send('Rを捧げさせてもらうぜ…')
    elif randnum == 8:
        await ctx.send('最速の彼方に行っちまったのか…')
    elif randnum == 9:
        await ctx.send('SouthYOKOHAMA…俺たちのSTREET…')
    elif randnum == 10:
        await ctx.send('伝説が始まる…')
    elif randnum == 11:
        await ctx.send('STREETを流してるとREWARDS目当ての走り屋がPASSINGしかけてくる…')
    elif randnum == 12:
        await ctx.send('ほんとに、すまねえ！いまのオレにはあやまることしかできねえ…')
    elif randnum == 13:
        await ctx.send('…夢を見てたんだ…')

@bot.command()
async def c(ctx):
    await ctx.send('The race will begin in 10 seconds!')
    time.sleep(5)
    await ctx.send('The race will begin in 5 seconds!')
    time.sleep(2)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)
    await ctx.send("Go!")

@bot.command()
async def ranking(ctx, arg):
    if "記録" in str(ctx.channel) or "きろく" in str(ctx.channel) or "record" in str(ctx.channel):
        user, user_id = speedrun.get_user(arg)
        send_str = '\n'.join(user)
        await ctx.send(send_str)
        if user_id == '':
            return
        user_data = speedrun.get_user_data(user_id)
        send_list = []
        game_id = ''
        count = 0
        for data in user_data:
            previous_id = game_id
            game_id = data.get('run').get('game')
            if previous_id != game_id:
                if not count == 0:
                    send_str = '\n'.join(send_list)
                    await ctx.send(send_str)
                    send_list.clear()
                count = count + 1
                send_list.append('\n' + speedrun.get_title(game_id))
            records = speedrun.get_records(data)
            if not records == '':
                send_list.append(records)
        if len(send_list) == 1:
            send_list.append('\n' + 'records is not found')
        send_str = '\n'.join(send_list)
        await ctx.send(send_str)
        send_str = '\n'.join(user)
        await ctx.send(f'{send_str} record is End')

bot.run(token)
