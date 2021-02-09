import discord
from discord.ext import commands

#client = commands.bot( command_prefix = ':')
#client = commands.bot(command_prefix = '!')
client = commands.bot( command_prefix = "p!")
@client.event



@client.command ()
async def hi( ctx ):
	await ctx.send ( 'send' )

@client.command ()
async def lol( ctx ):
	await ctx.send ( 'lololoshka' )


token = "Nzg0MzAyMjY1ODcxMzY4MTky.X8nUZw.XEc8PacaFXvNuVnfY1h3Cg3ihfk"

client.run(token)
