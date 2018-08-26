#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep
import contextlib
import io
import time
import datetime
import math
import inspect
import textwrap
from discomaton.factories import bookbinding
import async_timeout



logging.basicConfig(level='INFO')
bot = commands.Bot(case_insensitive=True, command_prefix='d!')
bot.load_extension("cogs.admin")
bot.remove_command('help')
bot.load_extension("cogs.fun")
bot.load_extension("cogs.more")
bot.load_extension("cogs.utility")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.api")
bot.load_extension("cogs.meta")



colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]
owner = [449666730680254516]
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
"""
def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
load_opus_lib()
"""








"""
@bot.command()
async def help(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name='★Fun★', value='`8ball, lenny, respect, ping, poll, choose, calculate`', inline=True)
    em.add_field(name='★More★', value='`bug, feedback, dbl`', inline=True)
    em.add_field(name='★Moderation★', value='`kick, ban, purge`', inline=True)
    em.add_field(name='★Utility★', value='`servericon, serverroles, serverinfo, playerinfo, avatar, support, about`', inline=True)
    em.set_footer(text="Use 'd!' before each command", icon_url=ctx.me.avatar_url)
    em.set_thumbnail(url=ctx.me.avatar_url)
    await ctx.send(embed=em)
"""


@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot


"""

@bot.command(aliases= ["kitten", "kitty"])
async def cat(ctx):
    fp = "cat/{}".format(random.choice(os.listdir("cat")))
    await ctx.send(file=discord.File(fp))
"""

@bot.listen()
async def on_ready():
          print('Logging in as', bot.user.name)






@bot.command()
async def invite(ctx):
    'Returns the bot invite link'
    em = discord.Embed(color=discord.Colour.orange())
    em.add_field(name='Invite TheDark', value='[Here]( https://discordapp.com/api/oauth2/authorize?client_id=482942398490738698&permissions=104082502&scope=bot )')
    await ctx.send(embed=em)











@bot.listen()
async def on_command_error(ctx, error):
    print(f'\'{ctx.author}\' used command \'{ctx.command}\' and got this error: \n-{error}')
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f' Hey, You are being ratelimited! Try again in** {int(error.retry_after)} **seconds!', delete_after=5)
    if isinstance(error, commands.NotOwner):
        return await ctx.send(' You do not own this bot!')
    if isinstance(error, commands.BadArgument):
        return await ctx.send(f' {error}')
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send(' You are missing permission to execute this command')
    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send(' I am missing permission to perform this command!')


"""
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def search(ctx, *, query):
    search = query
    URL = 'https://www.google.com/search?q='
    words = search.split(" ")

    num = 0
    for w in words:
        if num is 0:
            URL = URL + w
            num = 1
        else:
            URL = URL + "+"+ w

    await ctx.send(URL)
    """













def cleanup_code(content):
    'Automatically removes code blocks from the code.'
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:(-1)])
    return content




async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        a = 0
        for i in bot.guilds:
            for u in i.members:
                if u.bot == False:
                    a = a + 1

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my favourite movie | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Game(name="with my friends | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="some music | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Game(name="with my new toys | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="zZStefan coding me | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.users)} users | d!help"))
        await sleep(30)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers | d!help"))
        await sleep(30)


















bot.loop.create_task(presence())
bot.run(os.getenv("TOKEN"))
