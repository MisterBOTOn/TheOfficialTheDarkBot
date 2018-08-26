from discord.ext import commands
from .utils import checks, formats
from .utils.paginator import HelpPaginator, CannotPaginate
import discord
from collections import OrderedDict, deque, Counter
import os, datetime
import asyncio
import copy
import unicodedata
import inspect



class Meta:
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)

    @commands.command(name='help')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _help(self, ctx, *, command: str = None):
        """Shows help about a command or the bot"""

        try:
            if command is None:
                p = await HelpPaginator.from_bot(ctx)
            else:
                entity = self.bot.get_cog(command) or self.bot.get_command(command)

                if entity is None:
                    clean = command.replace('@', '@\u200b')
                    return await ctx.send(f'Command or category "{clean}" not found.')
                elif isinstance(entity, commands.Command):
                    p = await HelpPaginator.from_command(ctx, entity)
                else:
                    p = await HelpPaginator.from_cog(ctx, entity)

            await p.paginate()
        except Exception as e:
            await ctx.send(e)



    @commands.command(aliases=['char'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def charinfo(self, ctx, *, characters: str):
        """Shows you information about a number of characters.
        -------------------
		Ex:
		d!charinfo :wave:
        """

        def to_string(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name not found.')
            return f'**{c}** | ``\\U{digit:>08}`` | {name}'
        msg = '\n'.join(map(to_string, characters))
        if len(msg) > 750:
            return await ctx.send('| Output too long to display.')
        await ctx.send(msg)









def setup(bot):
    bot.add_cog(Meta(bot))
