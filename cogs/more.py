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


class More():
	def __init__(self, bot):
		self.bot = bot



	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	async def discordbotlist(self, ctx):
		'Returns the bot DBL link'
		em = discord.Embed(title="", color=discord.Colour.blue())
		em.add_field(name="Discord Bot List", value='[TheDark]( https://www.youtube.com/channel/UCe3cJzGyLmIvqp0fj5PHwew?view_as=subscriber )', inline=False)
		
		await ctx.send(embed=em)






	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.command()
	async def feedback(self, ctx, *, feedback=None):
		'''Send your feedback to the bot creators
		-------------------
		Ex:
		d!feedback [feedback]'''
		if feedback is None:
			await ctx.send(' | Hey, please do `d!feedback <feedback>`')
		if feedback is not None:
			await self.bot.get_guild(481842101844443146).get_channel(481842101844443146).send(f'{ctx.author} ({ctx.author.id}) reported: {feedback}')
			await ctx.send(' | Your feedback was reported to the team')










	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.command()
	async def bug(self, ctx, *, bug=None):
		'''Report a bug
		-------------------
		Ex:
		d!bug [bug]'''
		if bug is None:
			await ctx.send(' | Hey, please do `d!bug <bug>`')
		if bug is not None:
			await self.bot.get_guild(481842101844443146).get_channel(481842101844443146).send(f'{ctx.author} ({ctx.author.id}) reported: {bug}')
			await ctx.message.channel.send('| Your problem was reported to the team')















































def setup(bot):
        bot.add_cog(More(bot))
