#Jose Vargas Figueroa
#SE126 Midterm Lab 5
#08/21/2024

#Program Prompt: Write a program that can be used by a small theater to sell tickets for performances.  The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken.  Seats thar are available are represented by # and seats that are taken are represent by a *. There are aisles after seats H and V. 

# The program should display the above seating map, with # to denote open seats and * to denote taken seats.  The user must enter the row and seat numbers for tickets being sold.
#Every time a ticket or group of tickets is purchased (meaning the user is prompted to enter the seat(s) they wish to choose) the program should also be also displaying the total ticket prices (see page 2 table for pricing) in addition to the current seating chart’s availability.
#Use a menu to allow your user to do more than just purchase tickets:
#	1. Purchase Seat(s)
#	2. View Total Ticket Sales
#	3. View Sales Information
#	4. Checkout
#	5. Quit
#	The program should keep a total of all ticket sales. The user should be given an option of viewing this amount (menu 2). 
#	The program should also give the user an option to see a list of how many seats have been sold, how many seats are available in each row, and how may seats are available in the entire theater (menu 3). 
#	The program should allow the user to “check out” ie purchase their tickets. This option should show the user how many tickets they’ve purchased, along with a summary of the seats they’ve chosen, and the total cost for the tickets. Prompt the user for their amount, display their change, and then reset the customer ticket counter – this means a new customer could purchase more tickets without restarting the program, but the Total Ticket Sales and the View Sales Information will stay unchanged.


#See rubric on next page for additional requirements, such as functions!

#	The price for tickets are calculated using the following;
#	Row 1 – Row 5 are  $200.00
#	Row 6 – Row 10 are $175.00
#	Row 11 – Row 15 are $150.00

import csv
import os#needed to for clear screen function
import time#needed for a time delay when screen is cleared

rows = []
seatsA = []
seatsB = []
seatsC = []
seatsD = []
seatsE = []
seatsF = []
seatsG = []
seatsH = []
row1 = []
seatsI = []
seatsJ = []
seatsK = []
seatsL = []
seatsM = []
seatsN = []
seatsO = []
seatsP = []
seatsQ = []
seatsR = []
seatsS = []
seatsT = []
seatsU = []
seatsV = []
row2 = []
seatsW = []
seatsX = []
seatsY = []
seatsZ = []
seats1 = []
seats2 = []
seats3 = []
seats4 = []

row1_5Cost = 200
row6_10Cost = 175
row11_15Cost = 150
totalCost = 0
ticketCounter = 0

#connect to file----------------------------
with open("Labs/W5Lab_theaterSeatingChart/seatingChart.csv") as csvfile:
    file = csv.reader(csvfile)

#
    for rec in file:
        seatsA.append(rec[0])
        seatsB.append(rec[1])
        seatsC.append(rec[2])
        seatsD.append(rec[3])
        seatsE.append(rec[4])
        seatsF.append(rec[5])
        seatsG.append(rec[6])
        seatsH.append(rec[7])
        row1.append(rec[8])
        seatsI.append(rec[9])
        seatsJ.append(rec[10])
        seatsK.append(rec[11])
        seatsL.append(rec[12])
        seatsM.append(rec[13])
        seatsN.append(rec[14])
        seatsO.append(rec[15])
        seatsP.append(rec[16])
        seatsQ.append(rec[17])
        seatsR.append(rec[18])
        seatsS.append(rec[19])
        seatsT.append(rec[20])
        seatsU.append(rec[21])
        seatsV.append(rec[22])
        row2.append(rec[23])
        seatsW.append(rec[24])
        seatsX.append(rec[25])
        seatsY.append(rec[26])
        seatsZ.append(rec[27])
        seats1.append(rec[28])
        seats2.append(rec[29])
        seats3.append(rec[30])
        seats4.append(rec[31])
#disconnect----------------------

def clear_terminal():#clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Welcome to Ticket Master!")
    print("--------------------------------")
    print("1. Purchase Seat(s)\n2. View Total Ticket Sales\n3. View Sales Information\n4. Checkout\n5. Quit\n\n")
    
    menuInput = input("Please Select Menu Option[1-5]: ")

    return menuInput




time.sleep(1)#delays clearing terminal
clear_terminal()

menuInput = menu()

time.sleep(1)#delays clearing terminal
clear_terminal()

while menuInput not in {"1","2","3","4","5"}:
    print("INVALID ENTRY")

    time.sleep(1)#delays clearing terminal
    clear_terminal()

    menuInput = menu()

while menuInput == "1":

    print(f"\n{"ROW":33} SEATS")
    print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

    for i in range(0, len(seatsA)):
        print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

    seatPick = input("\nPlease enter seat section[A-Z,1-4]: ").lower()
    while seatPick not in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4"}:
        print("INVALID ENTRY")

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

        seatPick = input("\nPlease enter seat section[A-Z,1-4]: ").lower()

    rowPick = input("Please enter row number[1-15]: ")
    while rowPick not in {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"}:
        print("INVALID ENTRY")

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")
        
        print(f"\nYou have chosen Seat Section {seatPick}")
        rowPick = input("Please enter row number[1-15]: ")

        time.sleep(1)#delays clearing terminal
        clear_terminal()

    
    if seatPick in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4"}:
        
        if int(rowPick) in {1,2,3,4,5,6,7,8,9,10,11,12,14,15}:
            #section a --------------------------------------------------------------------
            if seatPick == "a":
                if seatsA[int(rowPick) - 1] != "X":
                    if int(rowPick) in {1,2,3,4,5}:
                        totalCost += row1_5Cost
                    elif int(rowPick) in {6,7,8,9,10}:
                        totalCost += row6_10Cost
                    elif int(rowPick) in {11,12,13,14,15}:
                        totalCost += row11_15Cost

                    seatsA[int(rowPick) - 1] = "X"
                    ticketCounter += 1
                    print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                else: print("\nSeat is taken, please pick another seat\n")
                time.sleep(2)#delays clearing terminal
                clear_terminal()


            #section b --------------------------------------------------------------------   
            elif seatPick == "b":
                if seatsB[int(rowPick) - 1] != "X":
                    if int(rowPick) in {1,2,3,4,5}:
                        totalCost += row1_5Cost
                    elif int(rowPick) in {6,7,8,9,10}:
                        totalCost += row6_10Cost
                    elif int(rowPick) in {11,12,13,14,15}:
                        totalCost += row11_15Cost

                    seatsB[rowPick - 1] = "X"
                    print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                else: print("\nSeat is taken, please pick another seat\n")

    else: print("INVALID ENTRY")
    time.sleep(1)#delays clearing terminal
    clear_terminal()


    print(f"{"ROW":33} SEATS")
    print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

    for i in range(0, len(seatsA)):
        print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

    menuInput = input("\nWould you like to purchase another ticket?[1. yes 2. no]: ")
    while menuInput not in {"1","2"}:
        print("INVALID ENTRY")
        time.sleep(1)#delays clearing terminal
        clear_terminal()
        menuInput = input("\nWould you like to purchase another ticket?[1. yes 2. no]: ")

        time.sleep(1)#delays clearing terminal
        clear_terminal()


time.sleep(1)#delays clearing terminal
clear_terminal()

menu()

#while menuInput == "2":


print(f"Total Amount Due: ${totalCost:.2f}")
print("\nThank You for using SeatMaster")