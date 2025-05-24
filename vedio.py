
import yt_dlp

url = input("Enter the YouTube video URL: ")

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
