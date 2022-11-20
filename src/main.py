import os
from datetime import datetime
from zoneinfo import ZoneInfo
import asyncio
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

# Time Zone, Channel Id
time_zones = [
]

@client.slash_command(description="Hello")
async def hello(interaction: discord.ApplicationContext):
    await interaction.respond('Pog', ephemeral=True)
    
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    while True:
        for channels in time_zones:
            channel_id = channels[2]
            time_zone = channels[1]
            suffix = channels[0]

            now = datetime.now(ZoneInfo(time_zone))
            time_string = f"🕒 {now.hour}:{now.minute} ({suffix})"
            await client.get_channel(channel_id).edit(name=time_string)

        await asyncio.sleep(1200)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client.run(DISCORD_TOKEN)
