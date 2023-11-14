import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check (ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f'Menyimpan gambar ke ./{attachment.filename}')
            hasil = get_class('keras_model.h5, 'labels.txt', f'.{/attachment.filename}')
            if hasil[0] == 'pigeon' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('burung ini memakan kacang, pisang dan semangka')
                await ctx.send('harga burung ini sekitaran IDR50k - IDR100k')
            elif hasil[0] == 'sparrow' and hasil[1] >= 0.65:
                await ctx.send(f'Gambar yang kamu kirim adalah {hasil[0]}')
                await ctx.send('burung ini memakan kacang, pisang dan semangka')
                await ctx.send('harga burung ini sekitaran IDR75k - IDR100k')
            else:
                await ctx.send ('GAMBAR MU KEMUNGKINAN: salah format/blur/corrupt')
                await ctx.send ('COBA MENGIRIM GAMBAR BARU!!!')
    else:
        await ctx.send('KAMU TIDAK MENGIRIM GAMBAR APAPUN :D')
bot.run("MTExMDU1Nzk5MzM3Nzk5MjcxNA.GDYyJ4.4w4qL3B9fu2B-hc1zBC4aTlRs37jTMuhStOYnQ")
