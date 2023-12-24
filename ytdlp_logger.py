import enlighten
import os
import logging

class YTDLPLogger:
    def __init__(self, count_songs, count_postprocessors):
        self.logger = logging.getLogger("enlighten")
        self.logger.setLevel(logging.ERROR)
        self.just_started = False
        self.just_started_post = False
        self.manager = enlighten.get_manager()
        self.title = self.manager.status_bar(status_format=u'Padufy Downloader',color='bold_underline_bright_white_on_webpurple',justify=enlighten.Justify.CENTER, demo='Initializing',)
        self.total_progress = self.manager.counter(total=count_songs,desc="Songs",unit="songs")
        self.song_progress = None
        self.song_post_progress = None
        self.count_postprocessors = count_postprocessors
        
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
        self.total_progress.update()
    
    def hook_download(self, data):
        filename = os.path.basename(data["filename"])[0:20]

        if not self.just_started:
            self.just_started = True
            self.song_progress = self.manager.counter(total=(data["total_bytes"]),
                                                      desc=filename,
                                                      unit="b", leave=False)
        

        if data["status"] == "finished":
            self.just_started = False
            self.total_progress.update()
            self.song_progress = None
            self.song_post_progress = self.manager.counter(total=self.count_postprocessors,
                                                      desc=str.rjust("Postprocessors",20),
                                                      unit="p", leave=False)
            return
        
        self.song_progress.update(incr=(data["downloaded_bytes"]-self.song_progress.count))
    
    def hook_post(self, data):
        #print(data.keys())
        #print(f"{data['status']} : {data['postprocessor']}")        
        if data["status"] == "finished":
            self.song_post_progress.update()