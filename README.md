🔥 JDDOS Testing Tool v2.0
<div align="center">
https://img.shields.io/badge/version-2.0-blue.svg?style=for-the-badge&logo=github
https://img.shields.io/badge/Python-3.x-green.svg?style=for-the-badge&logo=python
https://img.shields.io/badge/License-Educational-red.svg?style=for-the-badge
https://img.shields.io/badge/Platform-Windows%2520%257C%2520Linux%2520%257C%2520Mac-orange.svg?style=for-the-badge

</div><p align="center"> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=3F9CFF&center=true&vCenter=true&width=435&lines=Professional+DDoS+Testing+Tool;Educational+Purpose+Only;Created+by+Jony" alt="Typing SVG" /> </p>
📋 Mundarija

🌟 Xususiyatlar
⚙️ O'rnatish
🚀 Ishga Tushirish
🎯 Hujum Turlari
📊 Real-time Statistika
⚠️ Ogohlantirish

🌟 Xususiyatlar
<div align="center">
🏷️ Xususiyat	📝 Tavsif
🎯 Aniq Nishon	IP va Port orqali to'g'ridan-to'g'ri hujum
🔄 4 xil Hujum	HTTP, TCP, UDP va Mixed rejimlar
⚡ Yuqori Tezlik	Multi-threading bilan sekundiga 1000+ so'rov
📊 Real-time Stats	Doimiy yangilanuvchi statistika
🛡️ Random User-Agent	HTTP hujumlarda aniqlanishdan saqlanish
⌨️ Interaktiv Menu	Foydalanuvchi uchun qulay interfeys
</div>

⚙️ O'rnatish
#1. Repositoryni yuklab olish
git clone https://github.com/Jonyprogrammer/JDDoS.git

#2. Toolga kirish
cd web-stress-cli

#3. Venv yaratish
python3 -m venv venv

#4. Venv ni aktiv qilish
source venv/bin/activate

#5. Kutubxonalarni yuklab olish
pip install -r requirements.txt

#6. Ishga tushirish
python ddos.py

🚀 Ishga Tushirish
# Oddiy ishga tushirish
python jddos.py

# Yoki to'g'ridan-to'g'ri parametrlar bilan
python jddos.py --target example.com --port 80 --rate 100 --type http

🎯 Hujum Turlari
<div align="center">
🏹 Tur	🔧 Texnika	📈 Samaradorlik	🎭 Daraja
HTTP Flood	GET/HEAD so'rovlari	⭐⭐⭐	L7
TCP SYN Flood	Ulanish so'rovlari	⭐⭐⭐⭐	L4
UDP Flood	Tasodifiy paketlar	⭐⭐⭐⭐⭐	L3
MIXED Mode	Kombinatsiyalangan	⭐⭐⭐⭐⭐	L3-L7
</div>

🔍 Batafsil:
🕸️ HTTP Flood (L7)
python
# Random User-Agent bilan HTTP so'rovlar
Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
Mozilla/5.0 (X11; Linux x86_64)

🔌 TCP SYN Flood (L4)
text
[SYN] ──> 🌐 Server
[SYN-ACK] <── Server
[ACK] ──> Ulanish o'rnatildi

📦 UDP Flood (L3)
text
📦────📦────📦────📦────📦
1400 byte random packet flood

📊 Real-time Statistika
🎯 TARGET: example.com:80 | ⚡ RPS: 245 | ✅ OK: 12453 | ❌ ERR: 234 | 📊 98.1% | ⏱️ 45s
Belgisi	Ma'nosi
🎯	Nishon manzili
⚡	Sekundiga so'rovlar (RPS)
✅	Muvaffaqiyatli so'rovlar
❌	Muvaffaqiyatsiz so'rovlar
📊	Muvaffaqiyat foizi
⏱️	Ishlagan vaqt
📈 Yakuniy Hisobot
text
==================================================
📊 FINAL REPORT
==================================================
🎯 Target: example.com:80
⏱️  Uptime: 120.5 seconds
⚡ Average RPS: 1,245
📈 Total Requests: 150,000
✅ Successful: 149,000 (99.3%)
❌ Failed: 1,000
==================================================

⚠️ Ogohlantirish
<div align="center">
🚫 BU TOOL FAQAT TA'LIMIY MAQSADLARDA YARATILGAN!

⚡ Qonuniy	❌ Noqonuniy
✅ O'z serveringizda sinash	❌ Birovning serveriga hujum
✅ Penetratsion test (ruxsat bilan)	❌ Ruxsatsiz test
✅ Akademik tadqiqot	❌ Zarar yetkazish
✅ Xavfsizlik sohasida o'rganish	❌ Noqonuniy faoliyat
</div>

⚖️ Qonuniy Oqibatlari:
🚨 Ruxsatsiz foydalanish jinoiy javobgarlikka tortiladi
🌍 Ko'p mamlakatlarda 3-10 yil gacha qamoq jazosi
💰 $500,000 gacha jarima
🔒 Internetdan butunlay uzilish
🛡️ To'g'ri Foydalanish

⭐ Star this repository if you find it useful! ⭐

</div>
📝 Litsenziya
© 2026 Jony. Barcha huquqlar himoyalangan.
Bu kod faqat o'rganish va ta'limiy maqsadlar uchun.
<div align="center">
👨‍💻 Created with ❤️ by Jony - March 2026
</div>
