#W3D2 - Data from a Text File to 1D Parallel Lists

import csv

records = 0

#create empty lists to store file data to
names = []
ages = []
colors = []
animals = []

#connected to file----------
with open("week3/classList_202140.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #file is a 2D list! more on this in W4 :D
        #rec is a LIST of data which represents one entire record within the file
        #inside of this block everything happens for EACH record in the file!

        records += 1

        #print(rec[0])

        #add file data from the record to respective lists --> .append()
        names.append(rec[0]) #adds to the end
        ages.append(int(rec[1]))
        colors.append(rec[2])
        animals.append(rec[3])

#disconnected from file----------

for i in range(0, records):
    #parallel lists are connected via same INDEX
    #i --> index

    #if my name is found in a certain record, so should my fave animal
    print(f"{names[1]}'s favorite animal is the {animals[i]}.")

for i in range(0, len(names)):
    print(f"{names[i]}'s favorite color is {colors[i].upper()}.")

i = 0
for value in names:
    print(f"{names[i]} was {value} years old in 2021.")
    i += 1

    elephant_count = 0
    for i in range(0, len(names)):
        if "elephant" in animals[i].lower():
            elephant_count += 1

print(f"There are {elephant_count} within the list.")

#hand populated list:
se126_roster = ["jared","Alex","Jose","Paige","Cooper","Braedin"]

se126_2D = [
    ["Jared", "SE126", "CYB300", "NE255", "ENG240"],
    ["Jose", "SE111", "SE126", "NE121", "EN200"],
    ["Alex", "SE111", "SE126", "NE121", "EN220"]
]