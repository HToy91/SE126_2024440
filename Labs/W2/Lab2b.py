#Jose Vargas Figueroa
#SE126 Lab 2b
#07/24/2024

#Program Prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

import csv

#Variable Dictionary
#ile = csv.reader(list)
#machine = rec[0] if "D" machine = "desktop" else = "Laptop"
#brand = rec[1] if "Dl" brand = "Dell" elif "Hp" brand = "HP" else brand = "Gateway"
#cpu = rec[2]
#ram = rec[3]
#disk1 = rec[4]
#numdisk = int(rec[5]) if numdisk is 1 disk2 = " " os = rec[6] year = rec[7]
#else disk2 = rec[6] os = rec[7] year = rec[8]


#-----MAIN CODE-----
with open("Labs/W2/lab2b.csv") as list:
    file = csv.reader(list)#assigns csv file to the variable file

    print(f"{'Type':10} {'Brand':10} {'CPU':10} {'RAM':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':9} {'YR'}")#headeer

    for rec in file:

        machine = rec[0]#Determines types of machine
        if rec[0] == "D":
            machine = "Desktop"
        else:
            machine = "Laptop"

        brand = rec[1]#determines brand
        if rec[1] == "DL":
            brand = "Dell"
        elif rec[1] == "HP":
            brand = "HP"
        else:
            brand = "Gateway"
        #gives the indexes a variable
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        numdisk = int(rec[5])

        #numdisk number determines the index for the following variables
        if numdisk == 1:
            #only 2 hdd
            disk2 = " "
            os = rec[6]
            year = rec[7]

        else:
            disk2 = rec[6]
            os = rec[7]
            year = rec[8]

        print(f"{machine:10} {brand:10} {cpu:10} {ram:10} {disk1:10} {numdisk}           {disk2:9} {os:9} {year}")