class Song:
    def __init__(self, title, artist, lyrics = "", subtitles = ""):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.subtitles = subtitles
        self.duration = 0

    def __str__(self) -> str:
        return self.artist + ' - ' + self.title
    
    @property
    def info(self):
        return self.__dict__
    
