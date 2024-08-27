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
seatsChosen = []

row1_5Cost = 200
row6_10Cost = 175
row11_15Cost = 150
totalCost = 0
ticketCounter = 0
seatsSold = 0
row1Available = 30
row2Available = 30
row3Available = 30
row4Available = 30
row5Available = 30
row6Available = 30
row7Available = 30
row8Available = 30
row9Available = 30
row10Available = 30
row11Available = 30
row12Available = 30
row13Available = 30
row14Available = 30
row15Available = 30

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

def rowAvailableFunc():
    if (int(rowPick) - 1) == 0:
        row1Available -= 1
    elif (int(rowPick) - 1) == 1:
        row2Available -= 1
    elif (int(rowPick) - 1) == 2:
        row3Available -= 1
    elif (int(rowPick) - 1) == 3:
        row4Available -= 1
    elif (int(rowPick) - 1) == 4:
        row5Available -= 1
    elif (int(rowPick) - 1) == 5:
        row6Available -= 1
    elif (int(rowPick) - 1) == 6:
        row7Available -= 1
    elif (int(rowPick) - 1) == 7:
        row8Available -= 1
    elif (int(rowPick) - 1) == 8:
        row9Available -= 1
    elif (int(rowPick) - 1) == 9:
        row10Available -= 1
    elif (int(rowPick) - 1) == 10:
        row11Available -= 1
    elif (int(rowPick) - 1) ==11:
        row12Available -= 1
    elif (int(rowPick) - 1) == 12:
        row13Available -= 1
    elif (int(rowPick) - 1) == 13:
        row14Available -= 1
    else:
        row15Available -= 1

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

anotherPurchase = "yes"
flag = "green"

while flag == "green":
    while menuInput == "1" and anotherPurchase == "yes":

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
                        seatsSold += 1

                        rowAvailableFunc()

                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section a end-----------------------------------------------------------------

                #section b --------------------------------------------------------------------
                if seatPick == "b":
                    if seatsB[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsB[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()

                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section b end-----------------------------------------------------------------

                #section c --------------------------------------------------------------------
                if seatPick == "c":
                    if seatsC[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsC[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()

                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section c end-----------------------------------------------------------------

                #section d --------------------------------------------------------------------
                if seatPick == "d":
                    if seatsD[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsD[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section d end-----------------------------------------------------------------

                #section e --------------------------------------------------------------------
                if seatPick == "e":
                    if seatsE[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsE[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section e end-----------------------------------------------------------------

                #section f --------------------------------------------------------------------
                if seatPick == "f":
                    if seatsF[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsF[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section f end-----------------------------------------------------------------

                #section g --------------------------------------------------------------------
                if seatPick == "g":
                    if seatsG[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsG[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section g end-----------------------------------------------------------------

                #section h --------------------------------------------------------------------
                if seatPick == "h":
                    if seatsH[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsH[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section h end-----------------------------------------------------------------

                #section i --------------------------------------------------------------------
                if seatPick == "i":
                    if seatsI[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsI[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section i end-----------------------------------------------------------------

                #section j --------------------------------------------------------------------
                if seatPick == "j":
                    if seatsJ[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsJ[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section j end-----------------------------------------------------------------

                #section k --------------------------------------------------------------------
                if seatPick == "k":
                    if seatsK[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsK[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section k end-----------------------------------------------------------------

                #section l --------------------------------------------------------------------
                if seatPick == "l":
                    if seatsL[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsL[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section l end-----------------------------------------------------------------

                #section m --------------------------------------------------------------------
                if seatPick == "m":
                    if seatsM[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsM[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section m end-----------------------------------------------------------------

                #section n --------------------------------------------------------------------
                if seatPick == "n":
                    if seatsN[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsN[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section n end-----------------------------------------------------------------

                #section o --------------------------------------------------------------------
                if seatPick == "o":
                    if seatsO[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsO[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section o end-----------------------------------------------------------------

                #section p --------------------------------------------------------------------
                if seatPick == "p":
                    if seatsP[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsP[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section p end-----------------------------------------------------------------

                #section q --------------------------------------------------------------------
                if seatPick == "q":
                    if seatsQ[int(rowPick) - 1] != "X":
                        if int(rowPick) in {1,2,3,4,5}:
                            totalCost += row1_5Cost
                        elif int(rowPick) in {6,7,8,9,10}:
                            totalCost += row6_10Cost
                        elif int(rowPick) in {11,12,13,14,15}:
                            totalCost += row11_15Cost

                        seatsQ[int(rowPick) - 1] = "X"
                        ticketCounter += 1
                        seatsSold += 1

                        rowAvailableFunc()
                        
                        seatsChosen.append(seatPick + rowPick)
                        print(f"\nSeat is booked! Amount due: ${totalCost:.2f}\n")

                    else: print("\nSeat is taken, please pick another seat\n")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()
                #section q end-----------------------------------------------------------------

        else: print("INVALID ENTRY")
        time.sleep(1)#delays clearing terminal
        clear_terminal()


        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

        anotherPurchase = input("\nWould you like to purchase another ticket?[yes/no]: ").lower()
        while anotherPurchase not in {"yes","no"}:
            print("INVALID ENTRY")

            time.sleep(1)#delays clearing terminal
            clear_terminal()

            anotherPurchase = input("\nWould you like to purchase another ticket?[yes/no]: ").lower()

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        if anotherPurchase == "yes":
            menuInput == 1

        else:
            menuInput = menu()

        time.sleep(1)#delays clearing terminal
        clear_terminal()

    time.sleep(1)#delays clearing terminal
    clear_terminal()

    while menuInput == "2":
        print(f"Total Number of Tickets Sold: {ticketCounter}")

        returnMenu = input("\nPress ENTER to return to Main Menu: ")

        time.sleep(2)#delays clearing terminal
        clear_terminal()

        while returnMenu != "":
            print("INVALID ENTRY")
            returnMenu = input("\nPress ENTER to return to Main Menu: ")

            time.sleep(2)#delays clearing terminal
            clear_terminal()

        if returnMenu == "":
            menuInput = menu()

            time.sleep(2)#delays clearing terminal
            clear_terminal()

    while menuInput == "3":
        print(f"Number of Seats Sold: {ticketCounter}")

        print(f"\n{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")

        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")
        print(f"\nSeats Available in Row 1:  {row1Available}")
        print(f"Seats Available in Row 2:  {row2Available}")
        print(f"Seats Available in Row 3:  {row3Available}")
        print(f"Seats Available in Row 4:  {row4Available}")
        print(f"Seats Available in Row 5:  {row5Available}")
        print(f"Seats Available in Row 6:  {row6Available}")
        print(f"Seats Available in Row 7:  {row7Available}")
        print(f"Seats Available in Row 8:  {row8Available}")
        print(f"Seats Available in Row 9:  {row9Available}")
        print(f"Seats Available in Row 10: {row10Available}")
        print(f"Seats Available in Row 11: {row11Available}")
        print(f"Seats Available in Row 12: {row12Available}")
        print(f"Seats Available in Row 13: {row13Available}")
        print(f"Seats Available in Row 14: {row14Available}")
        print(f"Seats Available in Row 15: {row15Available}")

        returnMenu = input("\nPress ENTER to return to Main Menu: ")

        time.sleep(2)#delays clearing terminal
        clear_terminal()

        while returnMenu != "":
            print("INVALID ENTRY")
            returnMenu = input("\nPress ENTER to return to Main Menu: ")

            time.sleep(2)#delays clearing terminal
            clear_terminal()

        if returnMenu == "":
            menuInput = menu()
            time.sleep(2)#delays clearing terminal
            clear_terminal()


    if menuInput == "4":
        seatsChosen_str = ', '.join(seatsChosen)
        print(f"Total Amount Due: ${totalCost:.2f} for {ticketCounter} ticket(s)")
        print(f"Seats Chosen: {seatsChosen_str}")
        
        try:
            enterAmount = float(input("\nEnter Pay Amount: $"))

        except ValueError:
            print("INVALID ENTRY")
            enterAmount = float(input("Enter Amount to Pay: $"))
        
        while enterAmount < totalCost:
            print("\nINVALID AMOUNT")
            enterAmount = float(input("\nEnter Pay Amount: $"))
        else:
            print("\nThank You for using SeatMaster")
            print("-------------------------------")
            change = abs(totalCost - enterAmount)
            print(f"Your change is ${change:.2f}")
            print("\nHave a Great Day!")

            flag = "red"

    if menuInput == "5":
        print("Thank You for Using SeatMaster")
        flag = "red"