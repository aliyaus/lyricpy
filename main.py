import os
import time 
from mxmatch import Musixmatch
from song import Song

def main():
  run_time = time.strftime("%Y%m%d_%H%M%S")
  MX_TOKEN = os.getenv('API_KEY')
  mx = Musixmatch(MX_TOKEN)
  song = Song("Starboy", "The Weeknd")
  print("Retrieving info for: ", song.__str__())
  try:
    tracks = mx.search_track(song)
    for song in tracks:
        print(song.info)
  except Exception as e:
    print(f"An error occurred: {e}")
  
if __name__ == "__main__":
  main()