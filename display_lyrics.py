import time 
import drivers
from time import sleep
import datetime
from q import MyCustomQueue
from utils import parse_time_and_clean_line, convert_mmssmmm_to_seconds, split_string

# a slight/buffer before displaying lyric 
DISPLAY_BUFFER = 1.5

def display_lyrics(lines, display, song_position=None):
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

  print("Starting lyrics now:", start_time)
  display.lcd_display_string("Playing lyrics now!", 1)   

  while not q.is_empty():
    line_time, line = q.peek()
    elapsed_time = time.time() - start_time
    elapsed_secs = "{:.3f}".format(elapsed_time)
    converted_line_time_to_seconds = "{:.3f}".format(convert_mmssmmm_to_seconds(line_time))
    if elapsed_secs == converted_line_time_to_seconds:
      display.lcd_clear()   
      line_time, line = q.dequeue()
      print(line_time, " | ", line)
      split_line = split_string(line, 20)
      l1, l2, l3, l4 = (split_line + [''] * 4)[:4]
      display.lcd_display_string(l1, 1)   
      display.lcd_display_string(l2, 2)      
      display.lcd_display_string(l3, 3)      
      display.lcd_display_string(l4, 4)
      time.sleep(DISPLAY_BUFFER)

  if q.is_empty():
    display.lcd_clear()   
    display.lcd_display_string("The song is over/:", 1) 