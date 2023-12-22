import os

FLAG_USE_API = True

FILENAME_SONGS_FOLDER = "padufy_songs"
FILENAME_ERROR_LOG = "error_log.json"
FILENAME_SONGS_JSON = "songs.json"

PATH_SCRIPT_FOLDER = os.path.dirname(__file__)
PATH_SONGS_JSON = os.path.join(PATH_SCRIPT_FOLDER, FILENAME_SONGS_JSON)
PATH_ERROR_LOGS = os.path.join(PATH_SCRIPT_FOLDER, FILENAME_ERROR_LOG)
PATH_WIN_SONGS_DIR = os.path.join("C:\\Users\\",os.getlogin(),"Music")
PATH_SONGS_DIR = None

#If not on windows, set songs folder path in same script dir
if os.path.exists(PATH_WIN_SONGS_DIR):
    PATH_SONGS_DIR = os.path.join(PATH_WIN_SONGS_DIR,FILENAME_SONGS_FOLDER)
else: 
    PATH_SONGS_DIR = os.path.join(PATH_SCRIPT_FOLDER,FILENAME_SONGS_FOLDER)
