import qrcode
import requests
from io import BytesIO
from pytube import YouTube
import re

# Youtube video linkini kullanıcıdan iste
video_link = input("Lütfen YouTube video linkini girin: ")
yt = YouTube(video_link)
video_title = yt.title

# Geçersiz karakterleri kaldırma
video_title = re.sub('[^0-9a-zA-ZğüşıöçĞÜŞİÖÇ\s]+', '', video_title)

# Qr kod oluşturma ve kaydetme
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(video_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{video_title}.png")
