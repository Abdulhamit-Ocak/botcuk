import discord
from discord.ext import commands 
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command(name='bilgi', help='Botun kurucu bilgisini verir.')
async def bilgi(ctx):
    bilgi_cvp = "Bu Bot, Bor Madenci 64 tarafından yapılmıştır. Botun yapılışı için https://github.com/Abdulhamit-Ocak/discord-boru/new/main adresini ziyaret edebilirsiniz!"

ekbilgiler = [
    "Mümkünse ambalajsız ürünler satın alın veya yeniden kullanılabilir ambalajlar kullanın.",
    "Tasarruflu elektronik eşyalar kullanın.",
    "Sıfır Atığı hayat felsefesi olarak benimseyin.",
    "Doğal ve Yerel ürünleri kullanmaya önem gösterin.",
    "Araba yerine toplu taşıma, bisiklet veya yürüyüş tercih edin.",
    "Discord moderatörü olup aşırı kilo almayın",
    "Kimyasal gübreler ve pestisitler kullanmadan organik tarım uygulamaları yapın."
]
ekbilgiler.message_content = True


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pingim : `{bot.latency * 1000}`ms')

@bot.event
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(pass_context=True)
@bot.commands.has_permissions(manage_roles=True)
async def rolekle(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name}, {user.name} isimli üyeye bir rol verdi: {role.name}")

@bot.command()
async def mem(ctx):
    with open(f'resimler/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)



@bot.event()
async def on_ready():
    activity = discord.Game(name="!yardım")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot çalışıyor.")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason="Kural Çiğneme"): # kullanıcıyı atma komutu
    await bot.kick(member) # atma
    await ctx.send(f'{member} kullanıcısı yasaklandı') # mesaj gönderme

bot.run("MTI3Njk3NTk1OTAwMTY2MTU2Mw.GduWNC.2twYa05HgVgA_YvU9ICAz_Hx9jL4uN_osWRu2c")
