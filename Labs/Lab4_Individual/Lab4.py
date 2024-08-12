#Jose Vargas Figueroa
#SE126 Lab 4 Individual
#08/12/2024

#Program Prompt:
#In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list: This means you will have 1D parallel lists for this file!
#Then:
# Process the lists to print the them as they appear in the file
#Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)
#Re-Process the lists to print each record fully with the House Mottos
#Re-process the lists to find the average age within the list, then
#Print the total number of people in the list
#Print the average age - rounded to a whole number {:.0f}
#Print tallies/final counts for each allegiance (Field4) 

#Variable Dictionary:
#firstName = []
#lastName = []
#age = []
#nickname = []
#houseAllegiance = []
#motto = []
#numAvg = []
#stark = 0
#baratheon = 0
#tully = 0
#watch = 0
#lannister = 0
#targaryen = 0
#avgAge = 0
#totalPeople = len(firstName)

import csv

#create empty lists
firstName = []
lastName = []
age = []
nickname = []
houseAllegiance = []
motto = []
numAvg = []

#connected to file----------
with open("Labs/Lab4_Individual/lab4A_GOT_NEW.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseAllegiance.append(rec[4])
#disconnect from file----------

print(f"{'First Name':10}\t{'Last Name':15}\t{'Age':5}\t{'Nickname':20}\t{'House Allegiance'}")
print("----------------------------------------------------------------------------------------------------------------------")
#process lists -->for loop
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{age[i]:}\t{nickname[i]:20}\t{houseAllegiance[i]}")

print("----------------------------------------------------------------------------------------------------------------------")

#starting amount for people in each House
stark = 0
baratheon = 0
tully = 0
watch = 0
lannister = 0
targaryen = 0

#assigns motto to each house and tally's up individuals
for i in range(0, len(firstName)):
    if houseAllegiance[i] == "House Stark":
        houseMotto = "Winter is Coming"
        stark += 1

    elif houseAllegiance[i] =="House Baratheon":
        houseMotto = "Ours is the fury"
        baratheon += 1

    elif houseAllegiance[i] == "House Tully":
        houseMotto = "Family. Duty. Honor"
        tully += 1

    elif houseAllegiance[i] == "Night's Watch":
        houseMotto = "And now my watch begins"
        watch += 1

    elif houseAllegiance[i] == "House Lannister":
        houseMotto = "Hear me roar!"
        lannister += 1

    else:
        houseMotto = "Fire and Blood"
        targaryen += 1

    #adds motto to respective lists
    motto.append(houseMotto)

#reprocess to print and display new data
print(f"{'First Name':10}\t{'Last Name':15}\t{'Age':5}\t{'Nickname':20}\t{'House Allegiance':10}\t{'House Motto'}")
print("----------------------------------------------------------------------------------------------------------------------")

#process lists --> for loop
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{age[i]:}\t{nickname[i]:20}\t{houseAllegiance[i]:20}\t{motto[i]}")

print("----------------------------------------------------------------------------------------------------------------------")

#process list to find age average for each record
avgAge = 0
for i in range(0, len(firstName)):
    avgAge += age[i] / len(age)

#amount of people is length of firstName
totalPeople = len(firstName)

print(f"Total Number of People: {totalPeople}")
print(f"Average Age: {avgAge:.0f}")
print(f"\nHouse Stark: {stark}\nHouse Baratheon: {baratheon}\nHouse Tully: {tully}\nNight's Watch: {watch}\nHouse Lannister: {lannister}\nHouse Targaryen: {targaryen}")

print("----------------------------------------------------------------------------------------------------------------------")