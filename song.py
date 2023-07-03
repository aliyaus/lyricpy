class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return self.artist + ' - ' + self.title
    
    @property
    def info(self):
        return self.__dict__
    
