## Definition of Config class

import json
import Folder
import pathlib as pl 


class Config():

    

    def __init__(self, path):
        assert path.resolve().exists()
        self.path = path.resolve()

        #for later
        self.folders= []
        self.title = ""
        self.comment = ""
        self.raw_data = {}

        self.build()
        
    ## PUBLIC METHODS

    def build(self):
        self._load()
        self.title = self.raw_data['title']
        self.comment = self.raw_data['comment']
        for l_folder in self.raw_data['folders']:
            self.folders.append(Folder.Folder(l_folder))


    # GET METHODS
    def get_title(self):
        return self.title

    def get_folders(self):
        return self.folders
    
    def get_comment(self):
        return self.comment

    def deploy(self, destination):
        counter_folder_successfully_created = 0
        for folder in self.folders:
            if folder.deploy(destination):
                counter_folder_successfully_created+=1

    def get_patterns(self):
        return ["*" + ext for ext in self.get_exts()]
        
    

    ## INTERNAL METHODS
    def _load(self):
        with self.path.open('r') as f:
            self.raw_data = json.load(f)

    def _dump(self):
        with self.path.open('w') as f:
            json.dump(self.raw_data, f, indent=4)

    def __str__(self):
        return f"{self.title}"

    def get_number_folders(self):
        return len(self.folders)
    
    def get_exts(self):
        exts=[]
        for folder in self.folders:
            exts+=folder.get_extentions()

        return exts

if __name__ == '__main__':
    path = pl.Path("/home/slash/Documents/Programmation/projets/DISTRIBUTION/old/configs/Configuration_Hybrid.json")
    c = Config(path)
    #c.deploy("../../TEST/destination")
    print(c.get_exts())
    print(c.get_patterns())
    