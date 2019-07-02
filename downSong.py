#Dependencies
#sudo apt install python3-pip
#pip3 install youtube_dl
#sudo apt-get install ffmpeg

# Repository Official: https://github.com/rg3/youtube-dl/blob/master/README.md#copyright

from __future__ import unicode_literals
import youtube_dl
import sys



class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def define_format(varFormat):
    if varFormat == 'mp3':
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': varFormat,
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook]}

        return ydl_opts
    else:
        ydl_opts = {
        'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': varFormat,  # one of avi, flv, mkv,mp4, ogg, webm
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook]}

        return ydl_opts    

def download(varYdl_opts):
    with youtube_dl.YoutubeDL(varYdl_opts) as ydl:
        file = open("list.txt", "r")
        for linkSong in file:
            ydl.download([''+linkSong+''])



print("Format to download file?")
varFormat = input()
download(define_format(varFormat))



