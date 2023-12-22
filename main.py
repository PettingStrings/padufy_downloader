#Author: Paduraru Danut Razvan
import enlighten
import os
from utils import *
from constants import *
import songs_service
from ytdlp_logger import YTDLPLogger as Logger
import json
import time

downloaded_songs_mp3 = []
to_download = songs_service.get_songs()
logger = None
error_logs = []

if not os.path.exists(PATH_SONGS_DIR):
    os.mkdir(PATH_SONGS_DIR)

downloaded_songs_mp3 = [filename_purifier(song.removesuffix(".mp3")) for song in os.listdir(PATH_SONGS_DIR) if song.endswith(".mp3")]

a = [k for k in to_download.keys() if "front" in k]

for song in downloaded_songs_mp3:
    to_download.pop(song, None)

del downloaded_songs_mp3

logger = Logger(len(to_download))

for song in to_download:
    title = filename_purifier(song)
    link = to_download[song]

    try:
        songs_service.download(os.path.join(PATH_SONGS_DIR,title), link, logger=logger, hooks=[logger.hook])
    except Exception as e:
        error_logs.append({"song":title, "error":str(e)})
        if "frontier" in song:
            print(e)
            exit()

with open(PATH_ERROR_LOGS,encoding="utf-8",mode="w") as error_log_file:
    json.dump(error_logs, error_log_file)