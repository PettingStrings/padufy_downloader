#Author: Paduraru Danut Razvan
import pytube
import pytube.exceptions
import json
import os
import pathvalidate

#removes illegal characters from file names
def filename_purifier(path):
    return pathvalidate.sanitize_filepath(path)

FILENAME_SONGS_FOLDER = "songs"
FILENAME_ERROR_LOG = "error_log.json"
FILENAME_SONGS_JSON = "songs.json"

PATH_SCRIPT_FOLDER = os.path.dirname(__file__)
PATH_SONGS_JSON = os.path.join(PATH_SCRIPT_FOLDER, FILENAME_SONGS_JSON)
PATH_ERROR_LOGS = os.path.join(PATH_SCRIPT_FOLDER, FILENAME_ERROR_LOG)
PATH_WIN_SONGS_DIR = os.path.join("C:\\Users\\",os.getlogin(),"Music")
PATH_SONGS_DIR = ""

downloaded_songs = []
songs = []
error_logs = []

#If not on windows, set songs folder path in same script dir
if os.path.exists(PATH_WIN_SONGS_DIR):
    PATH_SONGS_DIR = os.path.join(PATH_WIN_SONGS_DIR,FILENAME_SONGS_FOLDER)
else: 
    PATH_SONGS_DIR = os.path.join(PATH_SCRIPT_FOLDER,FILENAME_SONGS_FOLDER)

if not os.path.exists(PATH_SONGS_DIR):
        os.mkdir(PATH_SONGS_DIR)

print("Downloading in: "+ PATH_SONGS_DIR)

for song in [song for song in os.listdir(PATH_SONGS_DIR) if song.endswith(".mp3")]:
    downloaded_songs.append(song.removesuffix(".mp3"))

with open(PATH_SONGS_JSON, encoding="utf-8") as file:
    songs = json.load(file)

for song in songs:
    title = filename_purifier(song["title"])
    link = song['link']

    if title in downloaded_songs:
        print("Skipping " + title)
        continue
    
    try:
        video = pytube.YouTube(link)
        audio = video.streams.filter(only_audio = True).first()

        audio.download(PATH_SONGS_DIR, filename=title+".mp3")
        print("DOWNLOADED: " + title)
    except Exception as e:
        error_logs.append({"song":title, "error":str(e)})
        print("===ERROR==: " + title)

print("Songs downloaded in "+ PATH_SONGS_DIR)

with open(PATH_ERROR_LOGS,encoding="utf-8",mode="w") as error_log_file:
    json.dump(error_logs, error_log_file)