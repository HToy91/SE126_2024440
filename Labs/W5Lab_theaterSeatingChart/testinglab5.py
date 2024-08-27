import csv
import os
import time

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

allSeats_chosen = []
totalCost = 0

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

ticketCounter = 0
seatsSold = 0

#connects to csv file
with open("Labs/W5Lab_theaterSeatingChart/seatingChart.csv") as csvfile:
    file = csv.reader(csvfile)

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
#disconnect

#function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Welcome to Ticket Master!")
    print("--------------------------------")
    print("1. Purchase Seat(s)\n2. View Total Ticket Sales\n3. View Sales Information\n4. Checkout\n5. Quit\n\n")
    mChoice = input("\nPlease select a Menu Option[1-5]: ")
    if mChoice not in {"1","2","3","4","5"}:
        time.sleep(1)
        clear_terminal()
        print("INVALID ENTRY")
        time.sleep(1)
        clear_terminal()
        print("Welcome to Ticket Master!")
        print("--------------------------------")
        print("1. Purchase Seat(s)\n2. View Total Ticket Sales\n3. View Sales Information\n4. Checkout\n5. Quit\n\n")
        mChoice = input("\nPlease select a Menu Option[1-5]: ")
    return mChoice

def sectionFunction():
    sChoice = input("\nPlease enter seat section: ").lower()
    while sChoice not in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4"}:
        time.sleep(1)
        clear_terminal()

        print("INVALID ENTRY")

        time.sleep(1)
        clear_terminal()

        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")
        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

        sChoice = input("\nPlease enter seat section: ").lower()
            
    return sChoice

def rowFunction():
    rChoice = input("Please enter row number: ").lower()
    while rChoice not in {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"}:

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        print("INVALID ENTRY")

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")
        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

        print(f"\nYou have chosen Seat Section {section_choice}")
        rChoice = input("Please enter row number[1-15]: ")
    return rChoice


answer = "y"

while answer.lower() == "y":
    menu_choice = menu()

    time.sleep(1)
    clear_terminal()

    while menu_choice == "1":
        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")
        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")

        section_choice = sectionFunction()
        row_choice = rowFunction()
        seats_chose = section_choice.upper() + row_choice

        if section_choice in {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4"}:
            if int(row_choice) in {1,2,3,4,5,6,7,8,9,10,11,12,14,15}:

                #section a----------------------------------------------------------------------------------------
                if section_choice == "a":#------------------------------->CHANGE LINE
                    if seatsA[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsA[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section a----------------------------------------------------------------------------------------

                #section b----------------------------------------------------------------------------------------
                if section_choice == "b":#------------------------------->CHANGE LINE
                    if seatsB[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsB[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section b----------------------------------------------------------------------------------------

                 #section c----------------------------------------------------------------------------------------
                if section_choice == "c":#------------------------------->CHANGE LINE
                    if seatsC[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsC[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section c----------------------------------------------------------------------------------------

                #section d----------------------------------------------------------------------------------------
                if section_choice == "d":#------------------------------->CHANGE LINE
                    if seatsD[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsD[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section d----------------------------------------------------------------------------------------

                #section e----------------------------------------------------------------------------------------
                if section_choice == "e":#------------------------------->CHANGE LINE
                    if seatsE[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsE[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section e----------------------------------------------------------------------------------------

                #section f----------------------------------------------------------------------------------------
                if section_choice == "f":#------------------------------->CHANGE LINE
                    if seatsF[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsF[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section f----------------------------------------------------------------------------------------

                #section g----------------------------------------------------------------------------------------
                if section_choice == "g":#------------------------------->CHANGE LINE
                    if seatsG[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsG[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section g----------------------------------------------------------------------------------------

                 #section h----------------------------------------------------------------------------------------
                if section_choice == "h":#------------------------------->CHANGE LINE
                    if seatsH[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsH[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section h----------------------------------------------------------------------------------------

                #section i----------------------------------------------------------------------------------------
                if section_choice == "i":#------------------------------->CHANGE LINE
                    if seatsI[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsI[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section i----------------------------------------------------------------------------------------

                #section j----------------------------------------------------------------------------------------
                if section_choice == "j":#------------------------------->CHANGE LINE
                    if seatsJ[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsJ[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section j----------------------------------------------------------------------------------------
        
                #section k----------------------------------------------------------------------------------------
                if section_choice == "k":#------------------------------->CHANGE LINE
                    if seatsK[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsK[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section k----------------------------------------------------------------------------------------

                #section l----------------------------------------------------------------------------------------
                if section_choice == "l":#------------------------------->CHANGE LINE
                    if seatsL[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsL[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section l----------------------------------------------------------------------------------------

                 #section m----------------------------------------------------------------------------------------
                if section_choice == "m":#------------------------------->CHANGE LINE
                    if seatsM[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsM[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section m----------------------------------------------------------------------------------------

                #section n----------------------------------------------------------------------------------------
                if section_choice == "n":#------------------------------->CHANGE LINE
                    if seatsN[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsN[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section n----------------------------------------------------------------------------------------

                #section o----------------------------------------------------------------------------------------
                if section_choice == "o":#------------------------------->CHANGE LINE
                    if seatsO[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsO[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section o----------------------------------------------------------------------------------------
        
                #section p----------------------------------------------------------------------------------------
                if section_choice == "p":#------------------------------->CHANGE LINE
                    if seatsP[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsP[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section p----------------------------------------------------------------------------------------

                #section q----------------------------------------------------------------------------------------
                if section_choice == "q":#------------------------------->CHANGE LINE
                    if seatsQ[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsQ[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section q----------------------------------------------------------------------------------------

                 #section r----------------------------------------------------------------------------------------
                if section_choice == "r":#------------------------------->CHANGE LINE
                    if seatsR[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsR[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section r----------------------------------------------------------------------------------------

                #section s----------------------------------------------------------------------------------------
                if section_choice == "s":#------------------------------->CHANGE LINE
                    if seatsS[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsS[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section s----------------------------------------------------------------------------------------

                #section t----------------------------------------------------------------------------------------
                if section_choice == "t":#------------------------------->CHANGE LINE
                    if seatsT[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsT[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section t----------------------------------------------------------------------------------------
        
                #section u----------------------------------------------------------------------------------------
                if section_choice == "u":#------------------------------->CHANGE LINE
                    if seatsU[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsU[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section u----------------------------------------------------------------------------------------

                #section v----------------------------------------------------------------------------------------
                if section_choice == "v":#------------------------------->CHANGE LINE
                    if seatsV[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsV[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section v----------------------------------------------------------------------------------------

                 #section w----------------------------------------------------------------------------------------
                if section_choice == "w":#------------------------------->CHANGE LINE
                    if seatsW[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsW[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section w----------------------------------------------------------------------------------------

                #section x----------------------------------------------------------------------------------------
                if section_choice == "x":#------------------------------->CHANGE LINE
                    if seatsX[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsX[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section x----------------------------------------------------------------------------------------

                #section y----------------------------------------------------------------------------------------
                if section_choice == "y":#------------------------------->CHANGE LINE
                    if seatsY[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsY[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section y----------------------------------------------------------------------------------------
        
                #section z----------------------------------------------------------------------------------------
                if section_choice == "z":#------------------------------->CHANGE LINE
                    if seatsZ[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seatsZ[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section z----------------------------------------------------------------------------------------

                #section 1----------------------------------------------------------------------------------------
                if section_choice == "1":#------------------------------->CHANGE LINE
                    if seats1[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seats1[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section 1----------------------------------------------------------------------------------------

                #section 2----------------------------------------------------------------------------------------
                if section_choice == "2":#------------------------------->CHANGE LINE
                    if seats2[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seats2[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section 2----------------------------------------------------------------------------------------

                #section 3----------------------------------------------------------------------------------------
                if section_choice == "3":#------------------------------->CHANGE LINE
                    if seats3[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seats3[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section 3----------------------------------------------------------------------------------------

                #section 4----------------------------------------------------------------------------------------
                if section_choice == "4":#------------------------------->CHANGE LINE
                    if seats4[int(row_choice) - 1] != "X":#------------------------------->CHANGE LINE
                        if int(row_choice) in {1,2,3,4,5}:
                                totalCost += 200
                        elif int(row_choice) in {6,7,8,9,10}:
                            totalCost += 175
                        else:
                            totalCost += 150

                        seats4[int(row_choice) - 1] = "X"#------------------------------->CHANGE LINE
                        ticketCounter += 1
                        seatsSold += 1

                        if (int(row_choice) - 1) == 0:
                            row1Available -= 1
                        elif (int(row_choice) - 1) == 1:
                            row2Available -= 1
                        elif (int(row_choice) - 1) == 2:
                            row3Available -= 1
                        elif (int(row_choice) - 1) == 3:
                            row4Available -= 1
                        elif (int(row_choice) - 1) == 4:
                            row5Available -= 1
                        elif (int(row_choice) - 1) == 5:
                            row6Available -= 1
                        elif (int(row_choice) - 1) == 6:
                            row7Available -= 1
                        elif (int(row_choice) - 1) == 7:
                            row8Available -= 1
                        elif (int(row_choice) - 1) == 8:
                            row9Available -= 1
                        elif (int(row_choice) - 1) == 9:
                            row10Available -= 1
                        elif (int(row_choice) - 1) == 10:
                            row11Available -= 1
                        elif (int(row_choice) - 1) ==11:
                            row12Available -= 1
                        elif (int(row_choice) - 1) == 12:
                            row13Available -= 1
                        elif (int(row_choice) - 1) == 13:
                            row14Available -= 1
                        else:
                            row15Available -= 1()

                        allSeats_chosen.append(seats_chose)
                        print(f"\nSeat {seats_chose} has been booked")

                        time.sleep(2)
                        clear_terminal()
                    else:
                        print(f"\nSeat {seats_chose} is taken, please pick another seat")

                        time.sleep(2)#delays clearing terminal
                        clear_terminal()
                #section 4----------------------------------------------------------------------------------------
        
        
        
        
        else:
            print("INVALID ENTRY")
            time.sleep(1)#delays clearing terminal
            clear_terminal()

        print(f"{"ROW":33} SEATS")
        print(f"     A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4")
        for i in range(0, len(seatsA)):
            print(f"{i + 1:3}  {seatsA[i]} {seatsB[i]} {seatsC[i]} {seatsD[i]} {seatsE[i]} {seatsF[i]} {seatsG[i]} {seatsH[i]} {row1[i]} {seatsI[i]} {seatsJ[i]} {seatsK[i]} {seatsL[i]} {seatsM[i]} {seatsN[i]} {seatsO[i]} {seatsP[i]} {seatsQ[i]} {seatsR[i]} {seatsS[i]} {seatsT[i]} {seatsU[i]} {seatsV[i]} {row2[i]} {seatsW[i]} { seatsX[i]} {seatsY[i]} {seatsZ[i]} {seats1[i]} {seats2[i]} {seats3[i]} {seats4[i]}")
                    
        anotherPurchase = input("\nWould you like to purchase another ticket?[y/n]: ").lower()
        while anotherPurchase not in {"y","n"}:
            time.sleep(1)#delays clearing terminal
            clear_terminal()

            print("INVALID ENTRY")

            time.sleep(1)#delays clearing terminal
            clear_terminal()

            anotherPurchase = input("\nWould you like to purchase another ticket?[yes/no]: ").lower()

        time.sleep(1)#delays clearing terminal
        clear_terminal()

        if anotherPurchase == "y":
            menu_choice == 1

        else:
            menu_choice = menu()

        time.sleep(1)#delays clearing terminal
        clear_terminal()                

    if menu_choice == "2":
        print(f"Total Number of Tickets Sold: {ticketCounter}")
        returnMenu = input("\nPress 'ENTER' to return to Main Menu: ")

        time.sleep(2)#delays clearing terminal
        clear_terminal()

        while returnMenu != "":
            print("INVALID ENTRY")
            returnMenu = input("\nPress 'ENTER' to return to Main Menu: ")

            time.sleep(2)#delays clearing terminal
            clear_terminal()

        if returnMenu == "":
            menuInput = menu()

            time.sleep(2)#delays clearing terminal
            clear_terminal()

    if menu_choice == "3":
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

    if menu_choice == "4":
        if totalCost >0:
            seatsChosen_str = ', '.join(allSeats_chosen)
            print(f"Total Amount Due: ${totalCost:.2f} for {ticketCounter} ticket(s)")
            print(f"Seats Chosen: {seatsChosen_str}")
            
            try:
                enterAmount = float(input("\nEnter Pay Amount: $"))

            except ValueError:
                print("INVALID ENTRY")
                enterAmount = float(input("Enter Pay Amount: $"))
            
            while enterAmount < totalCost:
                time.sleep(1)
                clear_terminal()
                
                print("\nINVALID AMOUNT")

                time.sleep(1)
                clear_terminal()

                print(f"Total Amount Due: ${totalCost:.2f} for {ticketCounter} ticket(s)")
                print(f"Seats Chosen: {seatsChosen_str}")
                try:
                    enterAmount = float(input("\nEnter Pay Amount: $"))

                except ValueError:
                    print("INVALID ENTRY")
                    enterAmount = float(input("Enter Pay Amount: $"))
            else:
                print("\nThank You for using SeatMaster")
                print("-------------------------------")
                change = abs(totalCost - enterAmount)
                print(f"Your change is ${change:.2f}")
                print("\nHave a Great Day!")

                answer = "n"
        else:
            print("Please purchase ticket")

            time.sleep(2)#delays clearing terminal
            clear_terminal()

    if menu_choice == "5":
        confirm = input("Are you sure?[y/n]: ").lower()

        time.sleep(1)
        clear_terminal()

        if confirm == "y":
            print("Thank you for using SeatMaster")
            answer =  "n"