import pandas as pd
from rapidfuzz import fuzz

lyrics = """
I'm tryna put you in the worst mood, ah
P1 cleaner than your church shoes, ah
Milli point two just to hurt you, ah
All red Lamb' just to tease you, ah
None of these toys on lease too, ah
Made your whole year in a week too, yeah
Main bitch outta your league too, ah
Side bitch out of your league too, ah
House so empty, need a centerpiece
Twenty racks a table cut from ebony
Cut that ivory into skinny pieces
Then she clean it with her face, man, I love my baby, ah
You talkin' money, need a hearing aid
You talkin' 'bout me, I don't see the shade
Switch up my style, I take any lane
I switch up my cup, I kill any pain
Look what you've done
I'm a motherfuckin' starboy
Look what you've done
I'm a motherfuckin' starboy
Every day a nigga try to test me, ah
Every day a nigga try to end me, ah
Pull off in that Roadster SV, ah
Pockets overweight, gettin' hefty, ah
Coming for the king, that's a far cry, ah
I come alive in the fall time, I
The competition, I don't really listen
I'm in the blue Mulsanne bumping New Edition
House so empty, need a centerpiece
Twenty racks a table cut from ebony
Cut that ivory into skinny pieces
Then she clean it with her face, man, I love my baby, ah
You talkin' money, need a hearing aid
You talkin' 'bout me, I don't see the shade
Switch up my style, I take any lane
I switch up my cup, I kill any pain
Look what you've done
I'm a motherfuckin' starboy
Look what you've done
I'm a motherfuckin' starboy
Let a nigga brag Pitt
Legend of the fall, took the year like a bandit
Bought mama a crib and a brand new wagon
Now she hit the grocery shop looking lavish
Star Trek roof in that Wraith of Khan
Girls get loose when they hear this song
A hundred on the dash get me close to God
We don't pray for love, we just pray for cars
House so empty, need a centerpiece
Twenty racks a table cut from ebony
Cut that ivory into skinny pieces
Then she clean it with her face, man, I love my baby, ah
You talkin' money, need a hearing aid
You talkin' 'bout me, I don't see the shade
Switch up my style, I take any lane
I switch up my cup, I kill any pain
Look what you've done
I'm a motherfuckin' starboy
Look what you've done
I'm a motherfuckin' starboy
Look what you've done
I'm a motherfuckin' starboy
Look what you've done
I'm a motherfuckin' starboy
"""

search_string = "You talkin' money, need a hearing aid You talkin' 'bout me, I don't see the shade"

def get_highest_string_match(array, search_string):
    df = pd.DataFrame(array, columns=['Line'])
    df['Percentage_Match'] = df['Line'].apply(lambda curr: fuzz.ratio(search_string, curr))
    max_match_percentage = df['Percentage_Match'].max()
    df = df[df['Percentage_Match'] >= max_match_percentage]
    print(df)
    return df.to_records()

print(get_highest_string_match(lyrics.split("\n"), search_string))