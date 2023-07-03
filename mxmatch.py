import json
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import constants
from song import Song


class Musixmatch:

    def __init__(self, token=None):
        self.token = token

    def search_track(self, song):
        """
        Searches for a track on the music API using the provided song's title and artist.

        Parameters:
        song (Song): An instance of the Song class containing the title and artist to be searched for.

        Returns:
        list: A list of Song instances matching the search criteria, each containing additional details about the song (i.e., ID, whether it has lyrics, and whether it has subtitles). 
              Returns an empty list if no match is found, and raises an exception if the API request is unsuccessful.

        Raises:
        Exception: If the status code from the API response indicates an unsuccessful request.
        """
        endpoint_path = "track.search"
        params = {
            "q_track": song.title,
            "q_artist": song.artist,
            "f_has_lyrics": 1,
            "f_has_subtitles": 1,
            "apikey": self.token
        }
        req = urllib.request.Request(constants.base_url + endpoint_path +
                                     "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote))
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
            song_title = tr["track_name"]
            song_artist = tr["artist_name"]
            song_id = tr["commontrack_id"]
            song_has_lyrics = tr["has_lyrics"]
            song_has_subtitles = tr["has_subtitles"]
            if song_id:
                tracks.append(Song(song_title, song_artist, song_id,
                              song_has_lyrics, song_has_subtitles))
        return tracks

    def get_lyrics(self, song):
        """
        Fetches the lyrics for a specific song from the music API using the song's commontrack_id.

        Currently, this function retrieves only the plain lyrics of the song. 

        TODO: Need to look into how to implement LRC style syncing with either the subtitle & translation method or another implementation.
        This would allow to sync the lyrics with the song's timing, providing a more dynamic and engaging experience for the user.
        The following endpoints provided by musixmatch include timestamps:
        * https://developer.musixmatch.com/documentation/api-reference/track-subtitle-translation-get
        * https://developer.musixmatch.com/documentation/api-reference/track-subtitle-get

        Parameters:
        song (Song): The Song object for which lyrics are to be fetched.

        Returns:
        str: The lyrics of the song, or None if the lyrics could not be fetched.
        """
        endpoint_path = "track.lyrics.get"
        params = {
            "commontrack_id": song.id,
            "apikey": self.token
        }

        req = urllib.request.Request(constants.base_url + endpoint_path +
                                     "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote))
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

        return body["body"]["lyrics"]["lyrics_body"]
