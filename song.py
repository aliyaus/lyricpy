class Song:
    def __init__(self, title, artist, id = "", has_lyrics = "", has_subtitles = ""):
        self.title = title
        self.artist = artist
        self.id = id
        self.has_lyrics = has_lyrics
        self.has_subtitles = has_subtitles

    def __str__(self) -> str:
        return self.artist + ' - ' + self.title
    
    @property
    def info(self):
        return self.__dict__
    
