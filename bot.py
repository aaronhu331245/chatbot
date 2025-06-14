import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
    

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def somma(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def sottrai(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def moltiplica(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def dividi(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def come_stai(ctx):
    await ctx.send(f'bene. faccioi la vita da bot.\U0001f642')

@bot.command()
async def arrivederci(ctx):
    await ctx.send("arrivederci! \U0001f642")

@bot.command()
async def leggi(ctx):   
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())

@bot.command()
async def scrivi(ctx):
    with open('text.txt', 'w', encoding='utf-8') as f:
        text = 'Questo è il testo che voglio inserire nel file'
        f.write(text)

@bot.command()
async def password(ctx, larghezza = 5):
    elements = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range (larghezza):
        password = password + random.choice(elements)
        await ctx.send(password)

@bot.command()
async def password_param(ctx, larghezza : int):
    elements = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range (larghezza):
        password = password + random.choice(elements)
        await ctx.send(password)

@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Una volta chiamato il comando dog, il programma richiama la funzione get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    '''Una volta chiamato il comando fox, il programma richiama la funzione get_fox_image_url'''
    fox_number = random.randint(1, 56)
    image_url = f'https://randomfox.ca/images/{fox_number}.jpg'
    await ctx.send(image_url)

@bot.command('pokemon')
async def pokemon(ctx):
    '''Una volta chiamato il comando pokemon, il programma invia un'immagine di un Pokémon casuale'''
    poke_number = random.randint(1, 151)
    image_url = ('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_number}.png').format(poke_number=poke_number)

    await ctx.send(image_url)

@bot.command('cat')
async def cat(ctx):
    '''Una volta chiamato il comando cat, il programma invia un'immagine di un gatto casuale'''
    cat_number = random.randint(1, 100)
    image_url = (f'https://cataas.com/cat?{cat_number}')
    
    await ctx.send(image_url)

@bot.command('musica')
async def musica(ctx):
    song_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    await ctx.send(song_url)

@bot.command('free_games')
async def free_games(ctx):
    free_games_url = 'https://www.epicgames.com/store/it/free-games'
    await ctx.send(f'Puoi trovare giochi gratuiti su Epic Games qui: {free_games_url}')

@bot.command(name='aiuto')
async def custom_help(ctx):
    help_text = (
        "Ecco i comandi disponibili:\n"
        "$ciao - Saluta il bot\n"
        "$heh [count] - Ripete 'he' per il numero specificato (default 5)\n"
        "$somma <left> <right> - Somma due numeri\n"
        "$sottrai <left> <right> - Sottrae due numeri\n"
        "$moltiplica <left> <right> - Moltiplica due numeri\n"
        "$dividi <left> <right> - Divide due numeri\n"
        "$come_stai - Chiede come sta il bot\n"
        "$arrivederci - Saluta il bot\n"
        "$leggi - Legge il contenuto di text.txt\n"
        "$scrivi - Scrive un testo in text.txt\n"
        "$password [larghezza] - Genera una password casuale (default 5 caratteri)\n"
        "$mem - Invia un'immagine memorizzata\n"
        "$meme - Invia un'immagine meme casuale\n"
        "$duck - Invia un'immagine di un'anatra casuale\n"
        "$dog - Invia un'immagine di un cane casuale\n"
        "$fox - Invia un'immagine di una volpe casuale\n"
        "$pokemon - Invia un'immagine di un Pokémon casuale\n"
        "$cat - Invia un'immagine di un gatto casuale\n"
        "$musica - Invia un link a una canzone su YouTube\n"
        "$free_games - Invia un link ai giochi gratuiti su Epic Games\n"
    )
    await ctx.send(help_text)

bot.run("inserisci il token")
