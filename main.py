import os
import time 
from mxmatch import Musixmatch
from song import Song
from utils import parse_time_and_clean_line, convert_mmssmmm_to_seconds, split_string
from q import MyCustomQueue

import syncedlyrics

import drivers
from time import sleep

def display_lyrics(lines):
  display = drivers.Lcd()
  q = MyCustomQueue()

  # parse timestamp and lyric from each line and push into queue
  for line in lines:
    line_time, cleaned_line = parse_time_and_clean_line(line)
    if line_time is not None:
      q.enqueue((line_time, cleaned_line))

  # Clear the LCD display 
  display.lcd_clear()   

  # Start clock 
  start_time = time.time() 
  print("playing...")

  while not q.is_empty():
    line_time, line = q.peek()
    elapsed_time = time.time() - start_time
    elapsed_secs = "{:.3f}".format(elapsed_time)
    converted_line_time_to_seconds = "{:.3f}".format(convert_mmssmmm_to_seconds(line_time))
    if elapsed_secs == converted_line_time_to_seconds:
      display.lcd_clear()   
      line_time, line = q.dequeue()
      split_line = split_string(line, 20)
      l1, l2, l3, l4 = (split_line + [''] * 4)[:4]
      display.lcd_display_string(l1, 1)   
      display.lcd_display_string(l2, 2)      
      display.lcd_display_string(l3, 3)      
      display.lcd_display_string(l4, 4)             


def main():
  run_time = time.strftime("%Y%m%d_%H%M%S")
  MX_TOKEN = os.getenv('API_KEY')
  mx = Musixmatch(MX_TOKEN)
  song = Song("Starboy", "The Weeknd")
  print("Retrieving info for: ", song.__str__())
  print()
  s = f"[{song.title}] [{song.artist}]"
  lrc = syncedlyrics.search(s)
  if lrc is not None:
    lines = lrc.split('\n')   
    display_lyrics(lines)
  else:
    display = drivers.Lcd()
    print("Unable to find song!") 
    display.lcd_display_string("Unable to find song!", 1)      
  
if __name__ == "__main__":
  main()