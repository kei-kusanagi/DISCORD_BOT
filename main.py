import os
from discord.ext import commands
from dotenv import load_dotenv
import discord
from pprint import pprint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="/")
cliente = discord.Client()


@bot.command(name='kei')
async def facebook(ctx):
    response = "https://www.facebook.com/keikusanagi99/"
    await ctx.send(response)
    print("se uso el comando !kei")


@bot.command(name='suma')
async def suma(ctx, num1, num2):
    suma = int(num1) + int(num2)
    await ctx.send(suma)


@bot.command(name='galleta')
async def galleta(ctx):
    response = "https: // orteil.dashnet.org / cookieclicker /"
    await ctx.send(response)


@bot.command(name='test')
async def test(ctx):
    response = "Hola soy un Robot"
    await ctx.send(response)
    print("se uso el comando !test")


@bot.command(name='teclado')
async def teclado(ctx):
    response = "https://www.keybr.com"
    await ctx.send(response)


@bot.event
async def on_message(mensaje):
    mensaje.content=mensaje.content.lower()
    pprint(mensaje)
    if mensaje.author.bot:
        return

    if mensaje.content.find("hora de salir") != -1:
        await mensaje.channel.send('https://media.giphy.com/media/7lyvQ60pEKBmE/giphy.gif')

    elif mensaje.content.find("encargo" and "robot") != -1:

        await mensaje.channel.send('🤖💬 Si mi creador, orale a trabajar!!!')
        await mensaje.channel.send('https://c.tenor.com/ayG-8y2NDRAAAAAM/whip-fire.gif')


    elif mensaje.content.find("clima") != -1:
        await mensaje.channel.send("🤖💬 Pues bien aunque aqui dentro de la compu siempre hace calor")

    elif mensaje.content.find("viernes") != -1:
        await mensaje.channel.send("https://c.tenor.com/tkF-EG9yB6gAAAAd/arigameplays-ari.gif")

    elif mensaje.content.find("hola") != -1:
        check=str(mensaje.author.nick)

        if check == "None":
            await mensaje.channel.send(f"🤖💬 Hola {mensaje.author.name} soy un robot")
        else:
            await mensaje.channel.send(f"🤖💬 Hola {mensaje.author.nick} soy un robot")

    elif mensaje.content.find("buenos") != -1:
        check=str(mensaje.author.nick)

        if check == "None":
            await mensaje.channel.send(f"🤖💬 Buenos dias {mensaje.author.name}")
        else:
            await mensaje.channel.send(f"🤖💬 Buenos dias {mensaje.author.nick}")

    elif mensaje.content.find("buenas") != -1:
        check=str(mensaje.author.nick)

        if mensaje.content.find("tardes") != -1:

            if check == "None":
                await mensaje.channel.send(f"🤖💬 Buenas tardes {mensaje.author.name}")
            else:
                await mensaje.channel.send(f"🤖💬 Buenas tardes {mensaje.author.nick}")

        if mensaje.content.find("noches") != -1:

            if check == "None":
                await mensaje.channel.send(f"🤖💬 Buenas noches {mensaje.author.name}")
            else:
                await mensaje.channel.send(f"🤖💬 Buenas noches {mensaje.author.nick}")


bot.run(TOKEN)
