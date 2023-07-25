import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
import time

# run the following in order to use this code 
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'

client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://localhost:8080'

scope = "user-read-playback-state"

def get_spotify_auth():
    # Try to load the token info from a file
    try:
        with open('token_info.json', 'r') as f:
            token_info = json.load(f)
    except (FileNotFoundError, IOError):
        token_info = None

    # If the token is expired or doesn't exist, go through the authorization process
    if token_info is None or token_info['expires_at'] < time.time():
        oauth = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            open_browser=False
        )

        print(f'Please navigate here: {oauth.get_authorize_url()}')

        response = input('Paste the above link here: ')
        code = oauth.parse_response_code(response)
        token_info = oauth.get_access_token(code)

        # Save the token info to a file
        with open('token_info.json', 'w') as f:
            json.dump(token_info, f)
    return token_info


def get_current_playing_song():
    token_info = get_spotify_auth()
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.current_playback()
    return {
        "title": results['item']['name'], 
        "album": results['item']['album']['name'],
        "current_timestamp": results['progress_ms'], 


    }

print(get_current_playing_song())