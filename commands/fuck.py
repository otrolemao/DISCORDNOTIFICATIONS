from discord.ext import commands

class Fuq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fuck(self, ctx, miembro: commands.MemberConverter):
        gif_url = "https://el.phncdn.com/pics/gifs/005/075/231/(m=ldpwiqacxtE_Ai)(mh=7QJ98SaqPYGc2qQ9)5075231b.gif"  # Cambia esto por tu GIF
        await ctx.send(f"{miembro.mention} {gif_url}")

async def setup(bot):
    await bot.add_cog(Fuq(bot))
