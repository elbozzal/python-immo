#Abstract : Créer un bot discord peu intelligent, et le dockerisé

import discord
from discord.ext import commands

intents = discord.Intents.all()
#client = discord.Client(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# Code du bot

@bot.event
async def on_ready():
        print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
        if message.author == bot.user:
                return
#       if str(message.author.id) == "AMI":
#               await message.channel.send('<:middle_finger:1112370247534657538>')
        if str(message.author.id) == "AMI":
                await message.add_reaction('\U0001F497')
        if 'test' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send('icule! O grand chef vénéré')
                else:
                        await message.channel.send('icule!')
        if 'donc' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send('et Kong! O grand chef vénéré')
                else:
                        await message.channel.send('et Kong!')
        if 'fuck you' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send('fuck you! O grand chef vénéré<:middle_finger:1112370247534657538>')
                else:
                        await message.channel.send('<:middle_finger:1112370247534657538>')
        if 'pouic' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send('pouic pouic! O grand chef vénéré')
                else:
                        await message.channel.send('pouic pouic!')
        if 'allo' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send(' à l huile! O grand chef vénéré')
                else:
                        await message.channel.send('à l huile!')
        if 'go' in message.content.lower():
                if str(message.author.id) == "CHEF":
                        await message.channel.send(' c est tipar! O grand chef vénéré')
                else:
                        await message.channel.send('c est tipar')
        # Lancement du bot
bot.run('TOKEN')
