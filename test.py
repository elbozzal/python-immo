import discord

# Création de l'objet client avec les intents appropriés
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Code du bot
@client.event
async def on_ready():
    print('Bot prêt à fonctionner')

@client.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('icule')

# Lancement du bot
client.run('MTEwMTU0OTM3MDEzMTg3Mzg2Mg.GJOjTU.a9ro0Ohs79AjhXnS6CtVAO_EZqTLqJtBSk0Muc')
