import discord
import random
from discord.ext import commands
import logging
import traceback
from datetime import datetime
import asyncio
import os
import aiohttp
from discord import opus
from asyncio import sleep
import datetime


class API():
	def __init__(self, bot):
		self.bot = bot




	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def doge(self, ctx):
		"""Generates a random image of a doge"""
		async with aiohttp.ClientSession() as cs:
			async with cs.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false') as r:
				res = await r.json()
				embed = discord.Embed(color=0x000000)
				embed.title = "Awww, a doge"
				embed.set_image(url=str(res).strip("[']"))
				embed.set_footer(text=f"Powered by shiba.online")
				embed.timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)




	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def dog(self, ctx):
		'Sends a image of a dog'
		async with aiohttp.ClientSession() as cs:
			async with cs.get("http://random.dog/woof.json") as r:
				res = await r.json()
				embed = discord.Embed(color=discord.Colour.red())
				embed.title = 'Cute dog :dog:'
				embed.set_image(url=res['url'])
				embed.set_footer(text=f"{self.bot.user.name}")
				embed.timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)












	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def cat(self, ctx):
		"""Generates a random image of a kitty"""
		async with aiohttp.ClientSession() as cs:
			async with cs.get('http://aws.random.cat/meow') as r:
				res = await r.json()
				embed = discord.Embed(color=0x000000)
				embed.title = "What a cute :cat:"
				embed.set_image(url=res['file'])
				embed.set_footer(text=f"{self.bot.user.name}")
				embed.timestamp = datetime.datetime.utcnow()
				await ctx.send(embed=embed)


























































































def setup(bot):
        bot.add_cog(API(bot))
