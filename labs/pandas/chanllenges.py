#!/usr/bin/python3

import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")
    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

   # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()

