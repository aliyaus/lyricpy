import speech_recognition as sr
import pyaudio
import pandas as pd
from rapidfuzz import fuzz

import sounddevice as sd
import soundfile as sf


lyrics = """
I'm tryna put you in the worst mood, ah
P1 cleaner than your church shoes, ah
Milli point two just to hurt you, ah
All red Lamb' just to tease you, ah
"""

def get_highest_string_match(array, search_string):
    df = pd.DataFrame(array, columns=['Line'])
    df['Percentage_Match'] = df['Line'].apply(lambda curr: fuzz.ratio(search_string, curr))
    max_match_percentage = df['Percentage_Match'].max()
    df = df[df['Percentage_Match'] >= max_match_percentage]
    print(df)
    return df.to_records()

# def get_vocals_from_audio(audio_file):
#     signal = nussl.AudioSignal(audio_file) 

#     seperator = nussl.Repet(signal)
#     seperator.run()

#     vocals = seperator.make_audio_signals()
#     output_file = 'temp/vocals.wav'
#     vocals[0].write_audio_to_file(output_file)
#     print("Separation complete. Vocals saved to:", output_file)
#     return output_file

def recognize_audio(audio_file):
    r = sr.Recognizer()

    # Load the audio file using the AudioFile class
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)  # Read the entire audio file

    # Use the recognize_google() function to transcribe the audio
    try:
        transcription_text = r.recognize_google(audio_data)
        return transcription_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def get_song_pos():
    # record sample audio for transcription 
    samplerate = 44100  
    duration = 5 
    output_file = 'temp/sample.wav'
    myrecording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until recording is finished

    # write sample recording to file path 
    sf.write(output_file, myrecording, samplerate)


    # Transcribe the audio file
    transcription_text = recognize_audio(output_file)

    if transcription_text:
        print("Transcription Text:", transcription_text)


get_song_pos()

    