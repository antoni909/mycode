#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""
    
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    nightmare= [
            {"slappy": "a", 
             "text": "b", 
             "kumquat": "goggles", 
             "user":{
                    "awesome": "c", 
                    "name": { "first": "eyes", "last": "toes"}
                    },
            "banana": 15, 
            "d": "nothing"
            }]
    
    goggles = challenge[2][0]
    eyes = challenge[2][1]
    print("My ", eyes, "! The ", goggles, "do nothing!")
    
    goggles = trial[2]["eyes"]
    eyes = trial[2]["goggles"]
    nothing = trial[-1]
    print("My ", eyes,"! The ", goggles, "do ",nothing,"!")

    goggles = nightmare[0]["kumquat"]
    eyes = nightmare[0]["user"]["name"]["first"]
    nothing = nightmare[0]["d"]
    print("My ", eyes,"! The ", goggles, "do ",nothing,"!")

if __name__ == "__main__":
    main()


