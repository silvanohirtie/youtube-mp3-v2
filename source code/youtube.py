from __future__ import unicode_literals
from os import system
import colored
from colored import stylize, fg, bg, attr
import youtube_dl
import platform
import ctypes
system = platform.system()
ctypes.windll.kernel32.SetConsoleTitleW("Youtube MP3 Downloader by Mental V2")
color = fg('red')
github = fg('blue')
credits = fg('green')
reset = attr('reset')
print(color + """█░░█ █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀▄ █▀▀   █▀▀▄ █▀▀█ █░░░█ █▀▀▄ █░░ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█
█▄▄█ █░░█ █░░█ ░░█░░ █░░█ █▀▀▄ █▀▀   █░░█ █░░█ █▄█▄█ █░░█ █░░ █░░█ █▄▄█ █░░█ █▀▀ █▄▄▀
▄▄▄█ ▀▀▀▀ ░▀▀▀ ░░▀░░ ░▀▀▀ ▀▀▀░ ▀▀▀   ▀▀▀░ ▀▀▀▀ ░▀░▀░ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀\n"""+reset)
print(credits+"V2 BY MENTAL\n"+reset)
print(github+"Github: https://github.com/Silvano-Hirtie/youtube-mp3-v2\n"+reset)
print("Insert the link:")
link = input("")
print("Insert the audio format (mp3,wav etc...):")
format = input("")
print("Insert the audio quality (128,192,320):")
quality = input("")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': format,
        'preferredquality': quality,
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Contact me on discord for any problem: https://discord.gg/BgjwgWx")
