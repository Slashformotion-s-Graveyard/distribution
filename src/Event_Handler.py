from watchdog.events import PatternMatchingEventHandler 

class Handler(PatternMatchingEventHandler):
    
    def on_modified(self, event):
        print("Le fichier %s a été modifié" % event.src_path)
    def on_created(self,event):
        print("Le fichier %s a été créé" % event.src_path)
    def on_deleted(self,event):
        print("Le fichier %s a été supprimé" % event.src_path)

    