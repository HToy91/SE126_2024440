#W4D2 - 1D, 2D Lists, Hand-Pipulation, Random, & Sequential Search

import random

#create some hand-populated 1D lists
dragon_names = [
    "Drogon",
    "Silverwing",
    "Vermithor",
    "Syrax",
    "Meleys"
]

#below list is PARALELL  -> if you find a dragon_name
dragon_alias = [
    "The Good Boi",
    "The Silver Lady",
    "The Bronze Fury",
    "The Goddess",
    "The Red Queen"
]

records = len(dragon_names) #records = 5

#simply display the paralell lists with each corresponding values on its own line
print(f"{"NAMES":12}    \t{"ALIAS"}")
print("---------------------------------")
for i in range(0, records):
    print(f"{dragon_names[i]:12} AKA \t{dragon_alias[i]}")
print("---------------------------------\n")

#use a random function to populate a new listss of dragon "ages"
dragon_ages = []
for i in range(0, len(dragon_names)):
    #"formal" way to add value to the lists
    dragon_ages.append(random.randint(0, 500))

for i in range(0, len(dragon_names)):
    print(f"{dragon_names[i]:12} AGE \t{dragon_ages[i]}")

#add all of the 1D lists to a new list, creating a 2D list!
'''
dragon_info = [
    dragon_names,
    dragon_alias,
    dragon_ages
]
'''

dragon_info = []
for i in range(0, len(dragon_names)):
    #print(f"{dragon_info[i]}")
    dragon_info.append([dragon_names[i], dragon_alias[i], dragon_ages[i]])

print("---DRAGON INFO & 2D LISTS-------------------------------")
#processing 2D lists (processing a list that is populated with more lists)
for i in range(0, len(dragon_names)):
    print(f"\nREC# {i} LIST: {dragon_info[i]}")#this prints the full list with ['', '']

    for x in range(0, len(dragon_info[i])):
        #for every item in the current list, display it! don't use i
        print(f"{dragon_info[i][x]:10}", end = " ")
        #end=" " removes new line at end of print()
    print()#creates a new line before next list in list
print("------------------------------------------------------")

#SEQUENTIAL SEARCH: to search "in sequence" --> from beginning [o] to end [len(listName) - 1]; use an IF to determine IF the search query is equal to a value within the list you're searching through

#get search value (query) from user
search_dragon = input("Who are you looking for?: ")

#create a variable to hold the "founder" data, if found
found = "n/a"

#search through the list to see if it's there
for i in range(0, len(dragon_names)):

    #SEARCH --> IF
    if search_dragon.lower() == dragon_names[i].lower():
        #store the INDEX to 'found' variable
        found = i
        break

#check to see if value has been found
if found != "n/a":
    print(f"Your search for {search_dragon} was FOUND in record #{found}")
    #display ALL data for found dragon
    print(f"NAME: {dragon_names[found]} \t ALIAS: {dragon_alias[found]} \t AGE: {dragon_ages[found]}")

else:
    print(f"Sorry, your search for {search_dragon} was *NOT* found")