base_url = "https://api.musixmatch.com/ws/1.1/"

status_codes = {
    404: 'Song not found.',
    401: 'Timed out. Change the token or wait a few minutes before trying again.',
    403: 'Forbidden. Not permitted.'
}