#Jose Vargas Figueroa
#SE126 Lab 3a
#07/29/2024

#Program Prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#Variable Dictionary

#Main Code
import csv

#initialize variable that willcount the total number of reords
records = 0

#empty lists
device = []
brand = []
cpu = []
ram = []
first_disk = []
second_disk = []
num_disks = []
os = []
yr = []

with open("W3_inClassLab/lab3a.csv") as list:
    file = csv.reader(list)#assigns csv file to the variable file

    print(f"{'Type':10} {'Brand':10} {'CPU':10} {'RAM':10} {'1st Disk':10} {'No HDD':10} {'2nd Disk':10} {'OS':9} {'YR'}")#header

    for rec in file:
        #update the records value
        records += 1

        #adds data to list
        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")
        else:
            device.append("-ERROR-")
            
        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == "DL":
            brand.append("Dell")
        else:
            brand.append("-BRAND ERROR-")
        
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disks.append(int(rec[5]))
        
        #not all records have 8 fields
        if int(rec[5]) == 1:
            second_disk.append("---")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            second_disk.append("-ERROR-")
            os.append(" @ ")
            yr.append(f"rec# {records}-")

#processes the lists to view their storage
for i in range(0, len(device)):
    #prints every index found in each list
    print(f"{device[i]:10} {brand[i]:10} {cpu[i]:10} {ram[i]:10} {first_disk[i]:10} {num_disks[i]}           {second_disk[i]:9} {os[i]:9} {yr[i]}")

#starts value from 0 and number of items in list is passed
desktops = 0
desktop_cost = 0
for i in range(0, len(device)):

    if device[i] == "Desktop":
        desktops += 1
        desktop_cost += 2000
print(f"\nTo replace {desktops} desktops it will cost $ {desktop_cost:5}.")

laptops = 0
laptop_cost = 0
for value in device:
    if value == "Laptop":
        laptops += 1
        laptop_cost += 1500
print(f"To replace {laptops} laptops it will cost $ {laptop_cost:5}.")
print(f"TOTAL: $ {(laptop_cost) + (desktop_cost)}")