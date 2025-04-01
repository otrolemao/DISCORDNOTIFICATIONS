import discord
from discord.ext import commands
import asyncio
from secreto import TOKEN  

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

# Cargar comandos desde la carpeta "commands"
async def load_extensions():
    await bot.load_extension("commands.hola")
    await bot.load_extension("commands.clear")
    await bot.load_extension("commands.notification")
    await bot.load_extension("commands.help_notifications")
    await bot.load_extension("commands.fuck")

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

# Iniciar el bot
asyncio.run(main())
