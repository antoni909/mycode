#!/usr/bin/env python3

import time
beer_count = int(input("How many bottles of beer?"))

continue_song = True

while continue_song:
    if beer_count > 100:
        print("must be less then 101 bottles")
    else:

        for count in range(beer_count,0,-1):
            print(f"{count} bottles  of beer on the wall!")
            time.sleep(4)
            print(f"{count} bottles of beer! You take one down, pass it around!")
            time.sleep(4)
        continue_song = False

