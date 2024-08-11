import csv

firstName = []
lastName = []
age = []
nickname = []
houseAllegiance = []
motto = []
numAvg = []

with open("Labs/Lab4_Individual/lab4A_GOT_NEW.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseAllegiance.append(rec[4])

print(f"{'First Name':10}\t{'Last Name':15}\t{'Age':5}\t{'Nickname':20}\t{'House Allegiance'}")
print("----------------------------------------------------------------------------------------")

for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{age[i]:}\t{nickname[i]:20}\t{houseAllegiance[i]}")

print("----------------------------------------------------------------------------------------")

for i in range(0, len(firstName)):
    if houseAllegiance[i] == "House Stark":
        houseMotto = "Winter is Coming"

    elif houseAllegiance[i] =="House Baratheon":
        houseMotto = "Ours is the fury"

    elif houseAllegiance[i] == "House Tully":
        houseMotto = "Family. Duty. Honor"

    elif houseAllegiance[i] == "Night's Watch":
        houseMotto = "And now my watch begins"

    elif houseAllegiance[i] == "House Lannister":
        houseMotto = "Hear me roar!"

    else:
        houseMotto = "Fire and Blood"

    motto.append(houseMotto)

print(f"{'First Name':10}\t{'Last Name':15}\t{'Age':5}\t{'Nickname':20}\t{'House Allegiance':10}\t{'House Motto'}")
print("----------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{age[i]:}\t{nickname[i]:20}\t{houseAllegiance[i]:20}\t{motto[i]}")

print("----------------------------------------------------------------------------------------------------------------------")