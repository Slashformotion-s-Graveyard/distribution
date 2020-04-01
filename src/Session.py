import datetime
import Logger
import pathlib

class Session():
    
    def __init__(self, logger):
        self.id = int()
        self.start_time = None
        self.stop_time = None
        self.nbr_synchro = int()  #number of synchronisation attempted
        self.title_config = str()
        self.path_logfile = pathlib.Path(f"")# mettre dedans la date
        



    def log_start(self):
        self.start_time = datetime.datetime.now()
        


    def log_stop(self):
        self.stop_stop = datetime.datetime.now()


