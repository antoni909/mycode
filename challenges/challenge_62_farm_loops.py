#!/usr/bin/env python3

farms = [
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
        ]

farms2 = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


#user_pick = input("pick one: NE Farm, W Farm, or SE Farm \n")
user_pick2 = input("pick one: Southwest Farm, Northeast Farm, East Farm, West Farm  \n")

plants_only = ["bananas", "apples", "oranges", "carrots", "celery"]


#for farm in farms:
#    if farm["name"] == user_pick:
#        if farm["name"] == "SE Farm"
#            print("carrots, "celery"")
#        else :
#            print(farm["agriculture"])

# iterate through farm2
for farm in farms2:
    # check against usrs input
    if farm["name"] == user_pick2:
        # iterate through agriculture array
        for el in farm["agriculture"]:
            # check against known plants elements
            if el not in plants_only:
                print(el) # print animals only

                
