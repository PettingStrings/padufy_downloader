from constants import *
import json
import requests
import yt_dlp
import utils

YTDLP_DEFAULT_OPTIONS =  {
        'writethumbnail': 'true',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegMetadata', 
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        {
            'key' : 'EmbedThumbnail',
            'already_have_thumbnail': False,
        }],
}

def get_songs():
    json_data = []
    
    if FLAG_USE_API:
        json_data = json.loads(requests.get("https://padurarudanutrazvan.altervista.org/api/v1/music-manager/song/get.php").text)
    else:
        with open(PATH_SONGS_JSON, encoding="utf-8") as file:
            json_data = json.load(file)

    return {utils.filename_purifier(item["title"]):item["link"] for item in json_data}

def prova(data):
    print(data)

def download(full_path,link, ytdlopt=YTDLP_DEFAULT_OPTIONS, logger=None, hooks=None):
    ytdlopt["outtmpl"] = full_path
    ytdlopt["logger"] = logger
    ytdlopt["progress_hooks"] = hooks
    ytdlopt["postprocessor_hooks"] = [prova]
    with yt_dlp.YoutubeDL(ytdlopt) as ydl:
        ydl.download([link])