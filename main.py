import os
import time 
from mxmatch import Musixmatch

def main():
  run_time = time.strftime("%Y%m%d_%H%M%S")
  MX_TOKEN = os.getenv('API_KEY')
  mx = Musixmatch(MX_TOKEN)
  body = mx.get_track()
  print(body) 
  


if __name__ == "__main__":
  print("hello")
  main()