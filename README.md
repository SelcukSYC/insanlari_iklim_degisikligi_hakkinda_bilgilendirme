🌍 İklim Değişikliği ve Yardımcı Discord Botu

Bu proje, iklim değişikliği farkındalığını artırmak ve temel matematiksel işlemleri gerçekleştirmek üzere Python ve discord.py kütüphanesi kullanılarak geliştirilmiş bir Discord botudur.

📌 Özellikler

$iklimbilgisi: Küresel ısınma, karbon ayak izi, sürdürülebilirlik ve çevre bilinci hakkında rastgele bilgilendirici mesajlar gönderir.

$iklimfoto: Proje dizininde yer alan iklimle ilgili görseli (foto.jpg) sunucuya gönderir.

$carpma <sayı1> <sayı2>: Verilen iki tam sayıyı çarpar.

$bolme <sayı1> <sayı2>: Verilen iki tam sayıyı böler (Sıfıra bölme hatasını kontrol eder).

🛠️ Gereksinimler

Projenin çalışabilmesi için sisteminizde Python 3.8 veya üzeri bir sürümün yüklü olması gerekmektedir. Ayrıca aşağıdaki Python paketleri kurulmalıdır:

discord.py

🚀 Kurulum ve Çalıştırma

Depoyu Klonlayın veya İndirin:
Proje dosyalarını bilgisayarınıza indirin.

Gerekli Bağımlılıkları Yükleyin:
Terminal veya Komut Satırını (CMD) açarak aşağıdaki komutu çalıştırın:

pip install discord.py


Görsel Dosyasını Hazırlayın:
Botun $iklimfoto komutunun sorunsuz çalışması için kod dosyasının bulunduğu dizine foto.jpg adında bir görsel eklediğinizden emin olun.

Botu Çalıştırın:
Bot ana dosyasını (örneğin main.py) çalıştırın:

python main.py


🔒 Güvenlik Notu

Botunuzun tokeni size özel bir anahtardır. Kodunuzu GitHub gibi açık kaynaklı ortamlarda paylaşmadan önce bot.run("TOKEN") kısmındaki token bilginizi gizlediğinizden veya .env dosyası/çevre değişkenleri kullandığınızdan emin olun.

📄 Lisans

Bu proje açık kaynaklıdır ve eğitim/farkındalık amaçlı geliştirilmiştir.
