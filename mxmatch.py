import json
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import constants
from song import Song

class Musixmatch:

    def __init__(self, token = None):
        self.token = token

    def search_track(self, song):
        endpoint_path = "track.search"
        params = {
            "q_track": song.title, 
            "q_artist": song.artist, 
            "f_has_lyrics": 1, 
            "apikey": self.token
        }
        req = urllib.request.Request(constants.base_url + endpoint_path + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote))
        try:
            response = urllib.request.urlopen(req).read()
        except (urllib.error.HTTPError, urllib.error.URLError, ConnectionResetError) as e:
            print(e)
            return
        
        r = json.loads(response.decode())

        if r['message']['header']['status_code'] != 200 and r['message']['header'].get('hint') == 'renew':
            print("Invalid token")
            return
        
        body = r["message"]

        status_code = body["header"]["status_code"]

        if status_code != 200:
            error_message = "API request could not be complete at this time."
            if status_code in constants.status_codes:
                error_message = constants.status_codes[status_code]
            raise Exception(error_message)
                

        tracklist_arr = body["body"]["track_list"]
        tracks = []
        for track in tracklist_arr:
            tr = track["track"]
            tracks.append(Song(tr["track_name"], tr["artist_name"]))
        return tracks
        
