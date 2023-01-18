#!/usr/bin/env python3
"""Returning Data From Complex JSON
    From the data returned, print out: question and answers
"""
import requests

URL= "https://opentdb.com/api.php?amount=3&category=9&difficulty=medium"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    resp= requests.get(URL).json()
    print(resp["results"])    
    
    for el in resp["results"]:
        print(el["question"])
        print(el["correct_answer"])

if __name__ == "__main__":
    main()

