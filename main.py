import os
import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

bilgiler = [
    "Gezegen Sıcaklığı Artıyor: Fosil yakıtların (kömür, petrol, doğalgaz) kontrolsüz kullanımı, sera gazı salınımını artırarak küresel ortalama sıcaklıkların yükselmesine neden olmaktadır.",
    "Kutuplar Hızla Eriyor: Yükselen sıcaklıklar nedeniyle kutuplardaki buzul kütleleri hızla erimekte ve deniz seviyeleri her yıl tehlikeli bir şekilde yükselmektedir.",
    "Aşırı Hava Olayları Sıklaşıyor: İklim değişikliği; daha şiddetli kasırgalara, beklenmedik sel baskınlarına ve uzun süren kuraklık dönemlerine yol açmaktadır.",
    "Orman Yaşam Kaynağımızdır: Ormansızlaşma, ağaçların atmosferdeki karbondioksiti yutma kapasitesini azaltarak iklim krizini daha da derinleştirmektedir.",
    "Deniz Ekosistemleri Tehdit Altında: Okyanusların daha fazla karbondioksit emmesi suların asitlenmesine neden olmakta, bu da mercan kayalıklarını ve deniz canlılarını yok etmektedir.",
    "Biyolojik Çeşitlilik Kayboluyor: Doğal yaşam alanlarının hızla değişmesi sebebiyle binlerce bitki ve hayvan türü neslinin tükenmesi riskiyle karşı karşıyadır.",
    "Su Kaynakları Azalıyor: Düzensiz yağış rejimi ve kuraklık, dünya genelinde tatlı su kaynaklarının hızla tükenmesine yol açmaktadır.",
    "Gıda Güvenliği Riski: Değişen mevsimler ve aşırı sıcaklar, tarımsal verimliliği düşürerek gelecekte küresel bir gıda krizine zemin hazırlamaktadır.",
    "İklim Göçleri Başladı: Kuraklık ve deniz seviyesinin yükselmesi gibi sebeplerle milyonlarca insan yaşanamaz hale gelen coğrafyalardan göç etmek zorunda kalmaktadır.",
    "Sağlığımızı Doğrudan Etkiliyor: Artan sıcaklık dalgaları, hava kirliliği ve yayılan salgın hastalıklar insan sağlığını ciddi şekilde tehdit etmektedir.",
    "Yenilenebilir Enerji Şart: Fosil yakıtlar yerine güneş, rüzgar ve jeotermal gibi temiz enerji kaynaklarına geçiş yapmak iklim krizini yavaşlatmanın en etkili yoludur.",
    "Bireysel Karbon Ayak İzi: Günlük hayatta enerji tasarrufu sağlamak, toplu taşıma kullanmak ve geri dönüşüme katkıda bulunmak bireysel karbon ayak izimizi azaltır.",
    "Plastik Ve Atık Yönetimi: Plastik atıkların azaltılması ve döngüsel ekonominin benimsenmesi, doğanın üzerindeki kirlilik baskısını önemli ölçüde hafifletir.",
    "Sürdürülebilir Tüketim: Yerel ve mevsiminde beslenmek, gereksiz tüketimden kaçınmak hem doğal kaynakları korur hem de emisyonları düşürür."
]


@bot.command()
async def carpma(ctx, left: int, right: int):
    """İki sayıyı çarpar."""
    await ctx.send(left * right)


@bot.command()
async def bolme(ctx, left: int, right: int):
    """İki sayıyı böler."""
    if right == 0:
        await ctx.send("Bir sayıyı 0'a bölemezsiniz.")
        return
    await ctx.send(left / right)


@bot.command()
async def iklimbilgisi(ctx):
    """Rastgele iklim bilgisi gönderir."""
    await ctx.send(random.choice(bilgiler))


@bot.command()
async def iklimfoto(ctx):
    """İklim fotoğrafını gönderir."""
    image_path = os.path.join(os.path.dirname(__file__), "foto.jpg")
    await ctx.send(file=discord.File(image_path))


@bot.event
async def on_ready():
    print(f"Bot giriş yaptı: {bot.user}")

bot.run("TOKEN")
