#Jose Vargas Figueroa
#SE126 Lab 2
#07/23/2024

#Program Prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#Variable Dictionary
#overCap = 0
#recordsProcessed = 0
#file = csv.reader(meetings)
#overAmount = int(record[1]) - int(record[2])

#-----MAIN CODE-----
import csv
overCap = 0
recordsProcessed = 0

#-----HEADER-----
print(f"{'Room':20} {' Max':10} {' Min':9} {'Over'}")

with open ("Labs/W2/lab2a.csv") as meetings:
    file = csv.reader(meetings)#assigns csv to the variable file
    

    for record in file:
        recordsProcessed += 1
        overAmount = int(record[1]) - int(record[2])#difference between max capacity and people attending
    
        if record[2] > record[1]:#if people attending is greater than max room capacity
            print(f"{record[0]:20} {record[1]:10} {record[2]:10} {abs(overAmount)}")
            overCap += 1   

    print(f"\n\nProcessed  {recordsProcessed}  records.")
    print(f"There are  {overCap}  rooms over the limit.")      
