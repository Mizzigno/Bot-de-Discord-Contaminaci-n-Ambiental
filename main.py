import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot de contaminación conectado")


@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que te informa sobre la contaminación ambiental.")
    await ctx.send("Usa el comando $guía para obtener información acerca del tema.")

@bot.command()
async def guía(ctx):
    await ctx.send("La contaminación ambiental es la presencia de sustancias nocivas en el medio ambiente que pueden causar efectos adversos en la salud humana y en los ecosistemas. Estas sustancias pueden ser químicas, físicas o biológicas y provienen de diversas fuentes, como la industria, el transporte, la agricultura y los residuos domésticos.")
    await ctx.send("Aquí te dejo una lista de comandos que puedes usar:")
    await ctx.send("- $glosario: Descubre qué significan los términos más importantes relacionados con la contaminación.")
    await ctx.send("- $casos: Conoce algunos casos de contaminación ambiental que han ocurrido en el mundo.")
    await ctx.send("- $minijuego: Aprende como clasificar los residuos de manera interactiva.")

@bot.command()
async def glosario(ctx, palabra: str):
    glosario = {
        "contaminación": "La presencia de sustancias nocivas en el medio ambiente.",
        "residuos": "Materiales desechados que pueden ser sólidos, líquidos o gaseosos.",
        "emisiones": "Liberación de sustancias contaminantes al aire, agua o suelo.",
        "ecosistema": "Conjunto de seres vivos y su entorno físico que interactúan entre sí.",
        "sostenibilidad": "Capacidad de mantener el equilibrio ecológico y satisfacer las necesidades presentes sin comprometer las futuras.",
        "biodegradable": "Capacidad de un material para descomponerse de manera natural por acción de microorganismos.",
        "reciclaje": "Proceso de convertir materiales desechados en nuevos productos para reducir"
    }
    significado = glosario.get(palabra.lower())
    if significado:
        await ctx.send(f"{palabra.capitalize()}: {significado}")
    else:
        await ctx.send("Lo siento, no tengo información sobre esa palabra en mi glosario.")

@bot.command()
async def casos(ctx):
    case = random.randint(1, 4)
    await ctx.send("Aquí tienes algunos casos de contaminación ambiental que han ocurrido en el mundo:")

    if case == 1:
        await ctx.send("Derrame de petróleo en el Golfo de México (2010): Uno de los mayores desastres ambientales, afectando la vida marina y las costas.")
        with open(f"images/conta/caso1.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif case == 2:
        await ctx.send("Contaminación del aire en Beijing, China: La ciudad ha enfrentado niveles peligrosos de smog debido a la industrialización y el tráfico vehicular.")
        with open(f"images/conta/caso2.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif case == 3:
        await ctx.send("Contaminación del agua en Flint, Michigan (2014): La crisis del agua potable debido a la presencia de plomo en el suministro de agua.")
        with open(f"images/conta/caso3.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif case == 4:
        await ctx.send("Deforestación en la Amazonía: La tala indiscriminada de árboles ha llevado a la pérdida de biodiversidad y al aumento de emisiones de carbono.")
        with open(f"images/conta/caso4.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

    @bot.command()
    async def minijuego(ctx):
        await ctx.send("¡Bienvenido al minijuego de clasificación de residuos!")
        await ctx.send("Te mostraré un residuo y tendrás que decirme si es reciclable o no.")
        await ctx.send("Escribe 'reciclable' o 'no reciclable' para responder.")

        residuos = {
            "Botella de plástico": "reciclable",
            "Papel usado": "reciclable",
            "Restos de comida": "no reciclable",
            "Lata de aluminio": "reciclable",
            "Vidrio roto": "reciclable",
            "Pañal desechable": "no reciclable"
        }

        residuo, respuesta_correcta = random.choice(list(residuos.items()))
        await ctx.send(f"Residuos: {residuo}")

        def check(m):
            return m.author == ctx.author and m.content.lower() in ["reciclable", "no reciclable"]

        try:
            mensaje = await bot.wait_for('message', check=check, timeout=15.0)
            if mensaje.content.lower() == respuesta_correcta:
                await ctx.send("¡Correcto! 🎉")
            else:
                await ctx.send(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}.")
        except asyncio.TimeoutError:
            await ctx.send("Se acabó el tiempo. Intenta nuevamente.")

    
