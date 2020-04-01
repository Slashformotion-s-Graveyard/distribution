## Definition of Folder class:
# 


import pathlib as pl 


class Folder():
    def __init__(self,infos):
        self.path = pl.Path(infos['path'])
        self.content = infos['content']
        self.extensions = infos['extensions']


    ## GET METHODS

    def get_extentions(self):
        return self.extensions

    def get_path(self):
        return self.path

    def get_comment(self):
        return self.get_comment
    
    def deploy(self, destination):
        try:
            path_to_deploy = destination / self.path
            path_to_deploy.mkdir()
        except FileExistsError as exception:
            return False
        else :
            return True
        
    ## INTERNAL METHODS

    def __str__(self):
        extensions = " ".join(self.get_extentions())
        return f"/{self.path} contient {self.content} correspondant aux extensions suivantes : {extensions}"


if __name__ == '__main__':
    infos= {
            "path": "Images",
            "content": "Images",
            "extensions": [
                ".jpg",
                ".jpeg",
                ".jpe",
                ".jif",
                ".jfif",
                ".jfi",
                ".png",
                ".gif",
                ".webp",
                ".raw",
                ".arw",
                ".cr2",
                ".nrw",
                ".k25",
                ".bmp",
                ".dib"
            ]
        }
    f = Folder(infos)
    assert type(f) is Folder 
    print(f)