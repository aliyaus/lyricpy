import os
import time 
from mxmatch import Musixmatch
from song import Song

import syncedlyrics

def main():
  run_time = time.strftime("%Y%m%d_%H%M%S")
  MX_TOKEN = os.getenv('API_KEY')
  mx = Musixmatch(MX_TOKEN)
  song = Song("Starboy", "The Weeknd")
  print("Retrieving info for: ", song.__str__())
  print()
  # try:
  #   tracks = mx.search_track(song)
  #   final_song = tracks[0]
  #   lyrics = mx.get_lyrics(final_song)
  #   print(lyrics)
  # except Exception as e:
  #   print(f"An error occurred: {e}")
  lrc = syncedlyrics.search("[Starboy] [The Weeknd]")
  print(lrc)
  
if __name__ == "__main__":
  main()