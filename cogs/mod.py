import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class Moderation():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]






	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member = None, *, reason = None):
		'''Ban a member in a guild
		-------------------
		Ex:
		d!ban @zZstefan Bad boy'''
		if member is None:
			await ctx.send("| Please provide a user to ban")
		if member == ctx.author:
			return await ctx.send("| You can't ban yourself!")
		if member == self.bot.user:
			return await ctx.send("| I can't ban myself!")
		if member == ctx.author.guild.owner:
			return await ctx.send("| I can't ban the owner")
		if member != ctx.author and member != self.bot.user:
			await member.ban()
			await ctx.send(f'| **{member}** just got banned.')





	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member = None, *, reason = None):
		'''Kick a member in a guild
		-------------------
		Ex:
		d!kick @zZstefan Shitposting'''
		if member is None:
			await ctx.send("| Please provide a user to kick")
		if member == ctx.author:
			return await ctx.send("| You can't kick yourself!")
		if member == self.bot.user:
			return await ctx.send("| I can't kick myself!")
		if member == ctx.author.guild.owner:
			return await ctx.send("| I can't kick the owner")
		if member != ctx.author and member != self.bot.user:
			await member.kick()
			await ctx.send(f'| **{member}** just got kicked.')

	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ["clear", "prune"])
	@commands.has_permissions(manage_guild=True)
	async def purge(self, ctx, number : int):
		'''Delete a number of messages in a channel
		-------------------
		Ex:
		d!purge 50'''
		if number>500 or number<0:
			return await ctx.send("| Invalid amount, maximum is 500.")
		await ctx.message.delete()
		await ctx.channel.purge(limit=number, bulk=True)
		await ctx.message.channel.send(f'| Succefully deleted {int(number)} messages!', delete_after=5)














































def setup(bot):
        bot.add_cog(Moderation(bot))
