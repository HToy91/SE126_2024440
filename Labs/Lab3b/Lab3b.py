#Jose Vargas Figueroa
#SE126 Lab 3b
#07/30/2024

#Program Prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

#VARIABLE DICTIONARY
#oldEnough_notReg = 0
#canVote_didnt = 0
#voters = 0
#recProcessed = 0
#cantRegA = []
#oldEnough_notRegA = []
#canVote_didntA = []
#votersA = []
#file = csv.reader(list)

#MAIN CODE
import csv

#initialize variable that will cound total number of records
cantReg = 0
oldEnough_notReg = 0
canVote_didnt = 0
voters = 0
recProcessed = 0

#empty list to append sums of previous variables
cantRegA = []
oldEnough_notRegA = []
canVote_didntA = []
votersA = []

with open("Labs/Lab3b/voters_202040.csv") as list:
    file = csv.reader(list)#assigns csv file to the variable file

    for rec in file:
        #updates values
        recProcessed += 1

        if int(rec[1]) < 18:
            cantReg += 1

        elif int(rec[1]) >= 18 and rec[2] == "N":
            oldEnough_notReg += 1

        elif rec[2] == "Y" and rec[3] == "N":
            canVote_didnt += 1
        elif rec[3] == "Y":
            voters += 1

    #adds sums of values and then .append
    cantRegA.append(cantReg)
    oldEnough_notRegA.append(oldEnough_notReg)
    canVote_didntA.append(canVote_didnt)
    votersA.append(voters)

    #processes the lists to view their storage
    for i in range(0, len(cantRegA)):
        print(f"                          Number of individuals not eligible to register: {cantRegA[i]:1}")
        print(f"Number of individuals who are old enough to vote but have not registered: {oldEnough_notRegA[i]:1}")
        print(f"         Number of individuals who are eligible to vote but did not vote: {canVote_didntA[i]:1}")
        print(f"                                      Number of individuals who did vote: {votersA[i]:1}")
        print("-----------------------------------------------------------------------------")

    print(f"                                             Number of records processed: {recProcessed}")