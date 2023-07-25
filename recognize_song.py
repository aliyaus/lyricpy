import os
import sounddevice as sd
import soundfile as sf
import numpy as np
import requests
import json

import asyncio
from shazamio import Shazam
from song import Song

def get_song_subtitles(url):
    response = requests.get(url)
    data = response.content
    return data

# TODO return error response if unable to recognize song 
async def decode_audio(output_file):
    shazam = Shazam()
    out = await shazam.recognize_song(output_file)
    return out

def recognize_song():
    print("starting song recognition")

    samplerate = 44100  
    duration = 10 
    # output file path 
    output_file = 'temp/output.wav'

    # get a sample recording 
    myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until recording is finished

    # write sample recording to file path 
    sf.write(output_file, myrecording, samplerate)

    print("Audio recorded and saved successfully.")

    loop = asyncio.get_event_loop()
    decoded_song = loop.run_until_complete(decode_audio(output_file))
    song_title = decoded_song['track']['title']
    song_artist = decoded_song['track']['subtitle']
    song_subtitles = get_song_subtitles(decoded_song["track"]['sections'][1]['url'])
    s = Song(song_title, song_artist, "", song_subtitles)
    return s

recognize_song()
