#!/usr/bin/env python3

import requests
import wget

def main2():
    
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    # NIKK
    print(f"{pokeapi['name']} image- {pokeapi['sprites']['front_default']}")
    imgurl= pokeapi['sprites']['front_default']

    # BONUS
    wget.download(imgurl, "/home/student/static/")

    # J
    for x in pokeapi['moves']:
        print(' >', x['move']['name'])

    # ETHAN
    print(f"{pokeapi['name']} has appeared in {len(pokeapi['game_indices'])} games!")

    # J
    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1

    print('This pokemon has appeared in', game_indices, 'video games')


def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    # sprites
    sprites = pokeapi["sprites"]['front_default']
    print(sprites)
    
    # moves
    moves = pokeapi["moves"]
    #print(moves)

    for dict_ in moves:
        print(dict_["move"]["name"])


    # game indices
    appeared_in = pokeapi["game_indices"]
    print(appeared_in)
    count = 0
    for dict_ in appeared_in:
        count += 1
    # count = len(appeared_in) 
    print(f'count: {count}')

main()
