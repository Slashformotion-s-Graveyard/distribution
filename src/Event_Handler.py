from watchdog.events import PatternMatchingEventHandler 
from Config import Config
from Logger import Logger
from pathlib import Path
import pathlib as pl
import shutil

class Handler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(self)
        self.logger = None
        self.config = None
        self.destination = None

    def set_process(self, config,logger, destination):
        try:
            assert isinstance(config, Config), "The config argument is not a Config instance"
            assert  isinstance(logger, Logger), "The logger argument is not a Logger instance"
            
        except AssertionError as error:
            print(error)
            return 0
        else:
            self.config = config
            self.logger = logger
            self.destination = destination

    def process(self, event):
        old_path = pl.Path(event.src_path)
        new_path = self.destination / self.config.build_file_path(old_path, self.logger)
        try:
            assert not new_path.exists(), f"New path for file ({old_path.name}) already exist"
        except AssertionError as error:
            self.logger.warning(error)
        else :
            shutil.move(old_path,new_path) 
    
    

    def on_modified(self, event):
        print("Le fichier %s a été modifié" % event.src_path)
        self.process(event)

    def on_created(self,event):
        print("Le fichier %s a été créé" % event.src_path)
    def on_deleted(self,event):
        print("Le fichier %s a été supprimé" % event.src_path)

    