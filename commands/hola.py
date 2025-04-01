from discord.ext import commands

class Hola(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hola(self, ctx):
        await ctx.send("q")

async def setup(bot):
    await bot.add_cog(Hola(bot))
