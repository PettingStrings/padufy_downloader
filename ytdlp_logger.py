import enlighten
import os
import logging

class YTDLPLogger:
    def __init__(self, count):
        self.logger = logging.getLogger("enlighten")
        self.just_started = False
        self.manager = enlighten.get_manager()
        self.title = self.manager.status_bar(status_format=u'Padufy Downloader',color='bold_underline_bright_white_on_webpurple',justify=enlighten.Justify.CENTER, demo='Initializing',)
        self.total_progress = self.manager.counter(total=count,desc="Songs",unit="songs")
        self.song_progress = None
        
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
        self.total_progress.update()
    
    def hook(self, data):
        filename = os.path.basename(data["filename"])[0:20]

        if not self.just_started:
            self.just_started = True
            self.song_progress = self.manager.counter(total=(data["total_bytes"]),
                                                      desc=filename,
                                                      unit="b", leave=False)
        
        self.song_progress.update(incr=(data["downloaded_bytes"]-self.song_progress.count))

        if data["status"] == "finished":
            self.just_started = False
            self.total_progress.update()
            self.song_progress = None