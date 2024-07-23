#Jose Vargas Figueroa
#SE126 Lab 2
#07/23/2024

import csv
overCap = 0
recordsProcessed = 0

with open ("Labs/W2/lab2a.csv") as meetings:
    file = csv.reader(meetings)

    for record in file:
        recordsProcessed += 1
        if record[2] > record[1]:
            print(f"{record}")
            overCap += 1         
