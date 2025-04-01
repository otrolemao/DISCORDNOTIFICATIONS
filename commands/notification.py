import discord
from discord.ext import commands, tasks
import json
import os
from datetime import datetime, timedelta

NOTIFICATIONS_FILE = "notifications.json"

class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_notifications.start()

    def load_notifications(self):
        if not os.path.exists(NOTIFICATIONS_FILE):
            with open(NOTIFICATIONS_FILE, "w") as file:
                json.dump([], file)

        with open(NOTIFICATIONS_FILE, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    return []
                return data
            except json.JSONDecodeError:
                return []

    def save_notifications(self, notifications):
        with open(NOTIFICATIONS_FILE, "w") as file:
            json.dump(notifications, file, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def notification(self, ctx, member: discord.Member, date: str, time: str, *, message: str):
        """Agrega una notificación: +notification @usuario DD/MM/YY HH:MM "mensaje" """
        try:
            notify_time = datetime.strptime(f"{date} {time}", "%d/%m/%y %H:%M")
        except ValueError:
            await ctx.send("❌ Formato incorrecto. Usa: +notification @usuario DD/MM/YY HH:MM \"mensaje\"")
            return

        notifications = self.load_notifications()
        notifications.append({
            "user_id": member.id,
            "timestamp": notify_time.timestamp(),
            "message": message
        })
        self.save_notifications(notifications)

        await ctx.send(f"✅ Notificación programada para {member.mention} en <t:{int(notify_time.timestamp())}:F>")

    @notification.error
    async def notification_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ No tienes permisos para usar este comando.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠️ Uso correcto: +notification @usuario DD/MM/YY HH:MM \"mensaje\"")
        else:
            await ctx.send("❌ Ha ocurrido un error. Verifica el formato e intenta de nuevo.")

    @tasks.loop(seconds=60)
    async def check_notifications(self):
        """Verifica las notificaciones cada minuto."""
        now = datetime.utcnow().timestamp()
        notifications = self.load_notifications()
        remaining_notifications = []

        for notification in notifications:
            if now >= notification["timestamp"]:
                user = self.bot.get_user(notification["user_id"])
                if user:
                    try:
                        embed = discord.Embed(
                            title="🔔 Recordatorio",
                            description=notification["message"],
                            color=discord.Color.blue()
                        )
                        await user.send(embed=embed)
                    except discord.Forbidden:
                        pass  # No puede enviar mensajes a este usuario
            else:
                remaining_notifications.append(notification)
        
        self.save_notifications(remaining_notifications)

    @check_notifications.before_loop
    async def before_check_notifications(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Notification(bot))
