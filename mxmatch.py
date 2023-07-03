import json
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import constants

class Musixmatch:

    def __init__(self, token = None):
        self.token = token

    def get_track(self):
        print("Getting track")
        endpoint_path = "track.get"
        params = {
            "commontrack_id": "5920049",
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

        if body["header"]["status_code"] != 200:
            if body["header"]["status_code"] == 404:
                print('Song not found.')
            elif body["header"]["status_code"] == 401:
                print('Timed out. Change the token or wait a few minutes before trying again.')
            else:
                print(f'Requested error: {body["matcher.track.get"]["header"]}')
            return

        return body["body"]["track"]
        
