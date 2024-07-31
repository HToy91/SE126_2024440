#Jose Vargas Figueroa
#SE126 Lab 3b
#07/30/2024

#Program Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

#VARIABLE and LIST DICTIONARY
#idNumber = []
#age = []
#registered = []
#voted = []
#cantReg = 0
#oldEnough_notReg = 0
#canVote_didnt = 0
#voters = 0
#records = 0

#MAIN CODE
import csv

#empty lists to store file data to
idNumber = []
age = []
registered = []
voted = []

#initialize variable that will count the total number of records
cantReg = 0
oldEnough_notReg = 0
canVote_didnt = 0
voters = 0
records = 0

with open("Labs/Lab3b/voters_202040.csv") as list:
    file = csv.reader(list)#assigns csv file to the variable file

    for rec in file:
        #updates values
        records += 1

        #adds file date from record to respective lists
        idNumber.append(rec[0])
        age.append(int(rec[1]))
        registered.append(rec[2])
        voted.append(rec[3])

    #for every index starting at 0 and up to the number of records
    for i in range(0, records):
        if age[i] < 18:
            cantReg += 1

        elif age[i] >= 18 and registered[i] == "N":
            oldEnough_notReg += 1

        elif registered[i] == "Y" and voted[i] == "N":
            canVote_didnt += 1
        elif voted[i] == "Y":
            voters += 1

    #processes the lists to view their storage
    print(f"                          Number of individuals not eligible to register: {cantReg}")
    print(f"Number of individuals who are old enough to vote but have not registered: {oldEnough_notReg}")
    print(f"         Number of individuals who are eligible to vote but did not vote: {canVote_didnt}")
    print(f"                                      Number of individuals who did vote: {voters}")
    print("-----------------------------------------------------------------------------")
    print(f"                                             Number of records processed: {records}")