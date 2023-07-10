import os
import time 
import argparse
from button_setup import button_setup
from song import Song
from display_lyrics import display_lyrics

import syncedlyrics

import drivers
from time import sleep

display = drivers.Lcd()
  
def on_button_press():
  song = Song("Lost", "Frank Ocean")
  display.lcd_display_string("Finding song...", 1) 
  print("Retrieving info for: ", song.__str__())
  print()
  s = f"[{song.title}] [{song.artist}]"
  lrc = syncedlyrics.search(s)
  if lrc is not None:
    lines = lrc.split('\n')  
    print("Song lyrics retrieved!") 
    display.lcd_display_string("Song lyrics retrieved XD", 1) 
    display_lyrics(lines, display)
  else:
    print("Unable to find song!") 
    display.lcd_display_string("Unable to find song!", 1)   

     
def main():
  # Set up argument parser
  parser = argparse.ArgumentParser(description="Lyricpy: display song lyrics synchronously. Uses a hardware button when the 'with_button' argument is passed.")
  parser.add_argument("with_button", help="Specify if button is used", choices=['with_button', 'normal'])
  args = parser.parse_args()

  if args.with_button == 'y':
      print("Running with button")
      BUTTON_PIN, prev_button_state = button_setup()
      try:
        print("ready to print lyrics!")
        while True: 
          time.sleep(0.1)
          button_state = GPIO.input(BUTTON_PIN)
          if button_state != prev_button_state:
            prev_button_state = button_state
            if button_state == GPIO.HIGH:
              on_button_press()
      except KeyboardInterrupt:
        print("program is exiting!")
        GPIO.cleanup()    
  else:
    print("Running without button")
    on_button_press() 
  
if __name__ == "__main__":
  main()