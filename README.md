# lyricpy

# Overview/Objective 
- on button click -> fetch lyrics for a single song -> sync the lyrics -> and display each line to LCD display

# Prerequisites 
### Generate Acoustid API Key 
1. run the following command in your terminal `export API_KEY="your_api_key"`
2. import API_KEY as follows:
```
import os
api_key = os.getenv('API_KEY')
```
* note to view the current exported API_KEY run `echo $API_KEY` 

### Install necessary dependencies 
1. run `pip install -r requirements.txt` 

# How to run 
1. to run with button run with the following command in your terminal `python3 main.py with_button` 
2. to run without button run with follwoing command `python3 main.py normal` 

# References 
* https://github.com/fashni/MxLRC
* https://github.com/akashrchandran/spotify-lyrics-api

#### Downstream APIs
* for lyric fetching - https://developer.musixmatch.com/documentation 

#### Connect LCD to Pi
* https://medium.com/@thedyslexiccoder/how-to-set-up-a-raspberry-pi-4-with-lcd-display-using-i2c-backpack-189a0760ae15

#### Setup SSH to Pi
* https://robertopozzi.medium.com/how-to-setup-ssh-to-connect-your-raspberry-pi-6dac4e454731

# Hardware 
* Raspberry Pi Model B (3rd generation & up) 
* IIC I2C TWI Serial LCD 2004 20x4 Display Module with I2C Interface Adapter Blue Backlight

# Future enhancements & ideas
- add LED lights to glow when device is listening to detect song 
- add song detection 
