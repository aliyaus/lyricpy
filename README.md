# lyricpy

# Overview/Objective 
- on button click -> fetch lyrics for a single song -> sync the lyrics -> and display each line to LCD display

# Prerequisites 
### Set API Key 
1. setup a musixmatch account and generate an API key
2. run the following command in your terminal `export API_KEY=your_api_key`
3. import API_KEY as follows: 
```
import os
api_key = os.getenv('API_KEY')
```

### Setup I2C with Raspberry Pi 
1. follow https://www.youtube.com/watch?v=3XLjVChVgec&t=122s for setup & driver installation 

# How to run 
1. run `pip install -r requirements.txt` to install required packages 
2. run the following command in your terminal `python3 main.py` 

# References 
* https://github.com/fashni/MxLRC
* https://github.com/akashrchandran/spotify-lyrics-api

#### Downstream APIs
* for lyric fetching - https://developer.musixmatch.com/documentation 

#### Connect LCD to Pi
* https://www.youtube.com/watch?v=3XLjVChVgec&t=122s

#### Setup SSH to Pi
* https://robertopozzi.medium.com/how-to-setup-ssh-to-connect-your-raspberry-pi-6dac4e454731

# Hardware 
* Raspberry Pi Model B (3rd generation & up) 
* IIC I2C TWI Serial LCD 2004 20x4 Display Module with I2C Interface Adapter Blue Backlight

# Future enhancements & ideas
- add LED lights to glow when device is listening to detect song 
- add song detection 
  - https://willdrevo.com/fingerprinting-and-audio-recognition-with-python/
  - https://github.com/worldveil/dejavu
