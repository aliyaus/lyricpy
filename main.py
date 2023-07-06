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
  s = f"[{song.title}] [{song.artist}]"
  lrc = syncedlyrics.search(s)
  print(lrc)
  
if __name__ == "__main__":
  main()