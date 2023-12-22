import requests
import json
import yt_dlp

data = json.loads(requests.get("https://padurarudanutrazvan.altervista.org/api/v1/music-manager/song/get.php").text)
data = [song for song in data if "index" in song["link"]]
infos = []
opt={
    "noplaylist":True,
    "key":"noplaylist"
}
with yt_dlp.YoutubeDL(opt) as ydl:
    for song in data:
        info=ydl.extract_info(song["link"], download=False)
        infos.append({
            "title":info["title"], "link":info["webpage_url"]
        })

with open("extracted.json","w") as f:
    json.dump(infos,f)