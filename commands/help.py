from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Help(self, ctx):
        await ctx.send("asd")

async def setup(bot):
    await bot.add_cog(Help(bot))