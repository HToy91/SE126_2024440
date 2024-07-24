#Jose Vargas Figueroa
#SE126 Lab 2
#07/23/2024

import csv
overCap = 0
recordsProcessed = 0

with open ("Labs/W2/lab2a.csv") as meetings:
    file = csv.reader(meetings)
    print("Room \t\tMax \tMin \tOver")

    for record in file:
        recordsProcessed += 1
        overAmount = int(record[1]) - int(record[2])
    
        if record[2] > record[1]:
            print(f"{record} {abs(overAmount)}")
            overCap += 1   

    print(f"\n\nProcessed {recordsProcessed} records.")
    print(f"There are {overCap} rooms over the limit.")      
