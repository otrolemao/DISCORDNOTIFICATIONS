import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)  # Solo admins pueden usarlo
    async def clear(self, ctx, cantidad: int):
        if cantidad <= 0:
            await ctx.send("❌ Ingresa un número válido mayor a 0.")
            return

        await ctx.channel.purge(limit=cantidad + 1)  # Borra los mensajes
        await ctx.send(f"✅ {cantidad} mensajes eliminados.", delete_after=3)  # Mensaje temporal

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ No tienes permisos de administrador para usar este comando.")

async def setup(bot):
    await bot.add_cog(Clear(bot))
