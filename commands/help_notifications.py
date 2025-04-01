import discord
from discord.ext import commands

class HelpNotifications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help_notifications")
    async def help_notifications(self, ctx):
        """Muestra ayuda sobre el comando de notificaciones"""
        embed = discord.Embed(
            title="📌 **Ayuda: Comando de Notificaciones**",
            description="Este comando te permite programar notificaciones privadas para los usuarios mencionados. ✉️🔔",
            color=discord.Color.blue()
        )
        embed.add_field(
            name="📢 **Uso del comando**",
            value='`+notification @usuario DD/MM/YY HH:MM "mensaje"`',
            inline=False
        )
        embed.add_field(
            name="📖 **Ejemplo**",
            value='`+notification @Oveja 28/04/25 13:48 "📅 Tienes una reunión importante 🕒"`',
            inline=False
        )
        embed.add_field(
            name="⚠️ **Notas**",
            value="🔹 Solo los administradores pueden usar este comando.\n"
                  "🔹 Asegúrate de escribir la fecha en el formato correcto.\n"
                  "🔹 El mensaje debe ir **entre comillas**.",
            inline=False
        )
        embed.set_footer(text="🤖 Bot de notificaciones - Usa +help para más comandos.")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpNotifications(bot))
