#Jose Vargas Figueroa
#SE126 Midterm
#08/13/2024

#Program Prompt:

import random
import csv
import os
import time

qbFirstName = []
qbLastName = []
qbOVR = [] #overall
qbSPD = [] #speed
qbSTR = [] #strength
qbAGI = [] #agility
qbJMP = [] #jumping
qbINJ = [] #injury
qbSTA = [] #stamina

#connect to quarterback list----------
with open("Midterm/qb.csv") as qb_csvfile:
    qbFile = csv.reader(qb_csvfile)

    for rec in qbFile:
        qbFirstName.append(rec[0])
        qbLastName.append(rec[1])
        qbOVR.append(rec[2])
        qbSPD.append(rec[3])
        qbSTR.append(rec[4])
        qbAGI.append(rec[5])
        qbJMP.append(rec[6])
        qbINJ.append(rec[7])
        qbSTA.append(rec[8])
#disconnect----------

teFirstName = []
teLastName = []
teOVR = [] #overall
teSPD = [] #speed
teSTR = [] #strength
teAGI = [] #agility
teJMP = [] #jumping
teINJ = [] #injury
teSTA = [] #stamina

#connect to tight end list----------
with open("Midterm/te.csv") as te_csvfile:
    teFile = csv.reader(te_csvfile)

    for rec in teFile:
        teFirstName.append(rec[0])
        teLastName.append(rec[1])
        teOVR.append(rec[2])
        teSPD.append(rec[3])
        teSTR.append(rec[4])
        teAGI.append(rec[5])
        teJMP.append(rec[6])
        teINJ.append(rec[7])
        teSTA.append(rec[8])
#disconnect---------

rtFirstName = []
rtLastName = []
rtOVR = [] #overall
rtSPD = [] #speed
rtSTR = [] #strength
rtAGI = [] #agility
rtJMP = [] #jumping
rtINJ = [] #injury
rtSTA = [] #stamina

#connect to right tackle list----------
with open("Midterm/rt.csv") as rt_csvfile:
    rtFile = csv.reader(rt_csvfile)

    for rec in rtFile:
        rtFirstName.append(rec[0])
        rtLastName.append(rec[1])
        rtOVR.append(rec[2])
        rtSPD.append(rec[3])
        rtSTR.append(rec[4])
        rtAGI.append(rec[5])
        rtJMP.append(rec[6])
        rtINJ.append(rec[7])
        rtSTA.append(rec[8])
#disconnect---------

rgFirstName = []
rgLastName = []
rgOVR = [] #overall
rgSPD = [] #speed
rgSTR = [] #strength
rgAGI = [] #agility
rgJMP = [] #jumping
rgINJ = [] #injury
rgSTA = [] #stamina

#connect to right guard list----------
with open("Midterm/rg.csv") as rg_csvfile:
    rgFile = csv.reader(rg_csvfile)

    for rec in rgFile:
        rgFirstName.append(rec[0])
        rgLastName.append(rec[1])
        rgOVR.append(rec[2])
        rgSPD.append(rec[3])
        rgSTR.append(rec[4])
        rgAGI.append(rec[5])
        rgJMP.append(rec[6])
        rgINJ.append(rec[7])
        rgSTA.append(rec[8])
#disconnect---------

ltFirstName = []
ltLastName = []
ltOVR = [] #overall
ltSPD = [] #speed
ltSTR = [] #strength
ltAGI = [] #agility
ltJMP = [] #jumping
ltINJ = [] #injury
ltSTA = [] #stamina

#connect to left tackle list----------
with open("Midterm/lt.csv") as lt_csvfile:
    ltFile = csv.reader(lt_csvfile)

    for rec in ltFile:
        ltFirstName.append(rec[0])
        ltLastName.append(rec[1])
        ltOVR.append(rec[2])
        ltSPD.append(rec[3])
        ltSTR.append(rec[4])
        ltAGI.append(rec[5])
        ltJMP.append(rec[6])
        ltINJ.append(rec[7])
        ltSTA.append(rec[8])
#disconnect---------

lgFirstName = []
lgLastName = []
lgOVR = [] #overall
lgSPD = [] #speed
lgSTR = [] #strength
lgAGI = [] #agility
lgJMP = [] #jumping
lgINJ = [] #injury
lgSTA = [] #stamina

#connect to left guard list----------
with open("Midterm/lg.csv") as lg_csvfile:
    lgFile = csv.reader(lg_csvfile)

    for rec in lgFile:
        lgFirstName.append(rec[0])
        lgLastName.append(rec[1])
        lgOVR.append(rec[2])
        lgSPD.append(rec[3])
        lgSTR.append(rec[4])
        lgAGI.append(rec[5])
        lgJMP.append(rec[6])
        lgINJ.append(rec[7])
        lgSTA.append(rec[8])
#disconnect---------

cFirstName = []
cLastName = []
cOVR = [] #overall
cSPD = [] #speed
cSTR = [] #strength
cAGI = [] #agility
cJMP = [] #jumping
cINJ = [] #injury
cSTA = [] #stamina

#connect to center list----------
with open("Midterm/c.csv") as c_csvfile:
    cFile = csv.reader(c_csvfile)

    for rec in cFile:
        cFirstName.append(rec[0])
        cLastName.append(rec[1])
        cOVR.append(rec[2])
        cSPD.append(rec[3])
        cSTR.append(rec[4])
        cAGI.append(rec[5])
        cJMP.append(rec[6])
        cINJ.append(rec[7])
        cSTA.append(rec[8])
#disconnect---------

hbFirstName = []
hbLastName = []
hbOVR = [] #overall
hbSPD = [] #speed
hbSTR = [] #strength
hbAGI = [] #agility
hbJMP = [] #jumping
hbINJ = [] #injury
hbSTA = [] #stamina

#connect to halfback list----------
with open("Midterm/hb.csv") as hb_csvfile:
    hbFile = csv.reader(hb_csvfile)

    for rec in hbFile:
        hbFirstName.append(rec[0])
        hbLastName.append(rec[1])
        hbOVR.append(rec[2])
        hbSPD.append(rec[3])
        hbSTR.append(rec[4])
        hbAGI.append(rec[5])
        hbJMP.append(rec[6])
        hbINJ.append(rec[7])
        hbSTA.append(rec[8])
#disconnect---------

wrFirstName = []
wrLastName = []
wrOVR = [] #overall
wrSPD = [] #speed
wrSTR = [] #strength
wrAGI = [] #agility
wrJMP = [] #jumping
wrINJ = [] #injury
wrSTA = [] #stamina

#connect to center list----------
with open("Midterm/wr.csv") as wr_csvfile:
    wrFile = csv.reader(wr_csvfile)

    for rec in wrFile:
        wrFirstName.append(rec[0])
        wrLastName.append(rec[1])
        wrOVR.append(rec[2])
        wrSPD.append(rec[3])
        wrSTR.append(rec[4])
        wrAGI.append(rec[5])
        wrJMP.append(rec[6])
        wrINJ.append(rec[7])
        wrSTA.append(rec[8])
#disconnect---------

#Functions----------
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def qbDecision(qbChoice):
    if qbChoice == "maye":
        qbChoice = qbFirstName[0] + qbLastName[0]
    elif qbChoice == "brissett":
        qbChoice = qbFirstName[1] + qbLastName[1]
    elif qbChoice == "zappe":
        qbChoice = qbFirstName[2] + qbLastName[2]
    elif qbChoice == "milton" or qbChoice == "milton iii":
        qbChoice = qbFirstName[3] + qbLastName[3]
    else:
        print("INVALID ENTRY")
        qbChoice = input("Please enter last name of starting quarterback: ").lower()

    return qbChoice

def teDecision(teChoice):
    if teChoice == "henry":
        teChoice = teFirstName[0] + teLastName[0]
    elif teChoice == "hooper":
        teChoice = teFirstName[1] + teLastName[1]
    elif teChoice == "bell":
        teChoice = teFirstName[2] + teLastName[2]
    elif teChoice == "wilcox":
        teChoice = teFirstName[3] + teLastName[3]
    elif teChoice == "cardona":
        teChoice = teFirstName[4] + teLastName[4]
    else:
        print("INVALID ENTRY")
        teChoice = input("Please enter last name of starting tight end: ").lower()

    return teChoice

def rtDecision(rtChoice):
    if rtChoice == "onwenu":
        rtChoice = rtFirstName[0] + rtLastName[0]
    elif rtChoice == "anderson":
        rtChoice = rtFirstName[1] + rtLastName[1]
    elif rtChoice == "wheatley" or rtChoice == "wheatley jr.":
        rtChoice = rtFirstName[2] + rtLastName[2]
    else:
        print("INVALID ENTRY")
        rtChoice = input("Please enter last name of starting right tackle: ").lower()

    return rtChoice

def rgDecision(rgChoice):
    if rgChoice == "sow":
        rgChoice = rgFirstName[0] + rgLastName[0]
    elif rgChoice == "robinson":
        rgChoice = rgFirstName[1] + rgLastName[1]
    else:
        print("INVALID ENTRY")
        rgChoice = input("Please enter last name of starting right guard: ").lower()

    return rgChoice

def ltDecision(ltChoice):
    if ltChoice == "okorafor":
        ltChoice = ltFirstName[0] + ltLastName[0]
    elif ltChoice == "wallace":
        ltChoice = ltFirstName[1] + ltLastName[1]
    elif ltChoice == "lowe":
        ltChoice = ltFirstName[2] + ltLastName[2]
    else:
        print("INVALID ENTRY")
        ltChoice = input("Please enter last name of starting left tackle: ").lower()

    return ltChoice

def lgDecision(lgChoice):
    if lgChoice == "strange":
        lgChoice = lgFirstName[0] + lgLastName[0]
    elif lgChoice == "leverett":
        lgChoice = lgFirstName[1] + lgLastName[1]
    elif lgChoice == "jordan":
        lgChoice = lgFirstName[2] + lgLastName[2]
    elif lgChoice == "mafi":
        lgChoice = lgFirstName[3] + lgLastName[3]
    else:
        print("INVALID ENTRY")
        lgChoice = input("Please enter last name of starting left guard: ").lower()

    return lgChoice

def cDecision(cChoice):
    if cChoice == "david andrews":
        cChoice = cFirstName[0] + cLastName[0]
    elif cChoice == "jake andrews":
        cChoice = cFirstName[1] + cLastName[1]
    else:
        print("INVALID ENTRY")
        cChoice = input("Please enter first and last name of starting center: ").lower()

    return cChoice

def hbDecision(hbChoice):
    if hbChoice == "stevenson":
        hbChoice = hbFirstName[0] + hbLastName[0]
    elif hbChoice == "gibson":
        hbChoice = hbFirstName[1] + hbLastName[1]
    elif hbChoice == "hasty":
        hbChoice = hbFirstName[2] + hbLastName[2]
    elif hbChoice == "harris":
        hbChoice = hbFirstName[3] + hbLastName[3]
    else:
        print("INVALID ENTRY")
        hbChoice = input("Please enter last name of halfback: ").lower()

    return hbChoice

def wrDecision(wrChoice):
    if wrChoice == "bourne":
        wrChoice = wrFirstName[0] + wrLastName[0]
    elif wrChoice == "smith-schuster":
        wrChoice = wrFirstName[1] + wrLastName[1]
    elif wrChoice == "douglas":
        wrChoice = wrFirstName[2] + wrLastName[2]
    elif wrChoice == "olsen":
        wrChoice = wrFirstName[3] + wrLastName[3]
    elif wrChoice == "polk":
        wrChoice = wrFirstName[4] + wrLastName[4]
    elif wrChoice == "reagor":
        wrChoice = wrFirstName[5] + wrLastName[5]
    elif wrChoice == "baker":
        wrChoice = wrFirstName[6] + wrLastName[6]
    elif wrChoice == "thornton":
        wrChoice = wrFirstName[7] + wrLastName[7]
    elif wrChoice == "boutte":
        wrChoice = wrFirstName[8] + wrLastName[8]
    elif wrChoice == "baker":
        wrChoice = wrFirstName[9] + wrLastName[9]
    else:
        print("INVALID ENTRY")
        wrChoice = input("Please enter last name of wide receiver: ").lower()

    return wrChoice
#---------------------------------------

#Main Code-----------------

print("Welcome to the Patriots starting line-up generator!")

generate = input("\nWould you like to generate a starting line-up? [y/n]: ").lower()

while generate != "y" and generate != "n":
    print("INVALID INPUT")
    generate = input("Would you like to generate a starting line-up? [y/n]: ").lower()

while generate == "y":
    name = input("\nPlease enter your name: ")
    print(f"Welcome {name}!")

#Pick your Quarterback---------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(qbFirstName)):
        print(f"{qbFirstName[i]:10}\t{qbLastName[i]:10}\t{qbOVR[i]}\t{qbSPD[i]}\t{qbSTR[i]}\t{qbAGI[i]}\t{qbJMP[i]}\t{qbINJ[i]}\t{qbSTA[i]}")

    qbStats = []
    for i in range(0, len(qbFirstName)):
        qbStats.append([qbFirstName[i], qbLastName[i], qbOVR[i], qbSPD[i], qbSTR[i], qbAGI[i], qbJMP[i], qbINJ[i], qbSTA[i]])
    
    roster = []

    qb_playerChoice = input("\nPlease enter last name of starting quarterback: ").lower()
    qb_starterChoice = qbDecision(qb_playerChoice)
    roster.append(qb_starterChoice)
    print(f"Great Choice, you picked {qb_starterChoice} as your starting Quarterback!")

    time.sleep(2)
    clear_terminal()
#-------------------------------

#Pick your Tight End----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(teFirstName)):
        print(f"{teFirstName[i]:10}\t{teLastName[i]:10}\t{teOVR[i]}\t{teSPD[i]}\t{teSTR[i]}\t{teAGI[i]}\t{teJMP[i]}\t{teINJ[i]}\t{teSTA[i]}")

    teStats = []
    for i in range(0, len(teFirstName)):
        teStats.append([teFirstName[i], teLastName[i], teOVR[i], teSPD[i], teSTR[i], teAGI[i], teJMP[i], teINJ[i], teSTA[i]])

    te_playerChoice = input("\nPlease enter last name of starting tight end: ").lower()
    te_starterChoice = teDecision(te_playerChoice)
    roster.append(te_starterChoice)
    print(f"Great Choice, you picked {te_starterChoice} as your starting Tight End!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Right Tackle----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(rtFirstName)):
        print(f"{rtFirstName[i]:10}\t{rtLastName[i]:10}\t{rtOVR[i]}\t{rtSPD[i]}\t{rtSTR[i]}\t{rtAGI[i]}\t{rtJMP[i]}\t{rtINJ[i]}\t{rtSTA[i]}")

    rtStats = []
    for i in range(0, len(rtFirstName)):
        rtStats.append([rtFirstName[i], rtLastName[i], rtOVR[i], rtSPD[i], rtSTR[i], rtAGI[i], rtJMP[i], rtINJ[i], rtSTA[i]])

    rt_playerChoice = input("\nPlease enter last name of starting right tackle: ").lower()
    rt_starterChoice = rtDecision(rt_playerChoice)
    roster.append(rt_starterChoice)
    print(f"Great Choice, you picked {rt_starterChoice} as your starting Right Tackle!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Right Guard----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(rgFirstName)):
        print(f"{rgFirstName[i]:10}\t{rgLastName[i]:10}\t{rgOVR[i]}\t{rgSPD[i]}\t{rgSTR[i]}\t{rgAGI[i]}\t{rgJMP[i]}\t{rgINJ[i]}\t{rgSTA[i]}")

    rgStats = []
    for i in range(0, len(rgFirstName)):
        rgStats.append([rgFirstName[i], rgLastName[i], rgOVR[i], rgSPD[i], rgSTR[i], rgAGI[i], rgJMP[i], rgINJ[i], rgSTA[i]])

    rg_playerChoice = input("\nPlease enter last name of starting right guard: ").lower()
    rg_starterChoice = rgDecision(rg_playerChoice)
    roster.append(rg_starterChoice)
    print(f"Great Choice, you picked {rg_starterChoice} as your starting Right Guard!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Left Tackle----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(ltFirstName)):
        print(f"{ltFirstName[i]:10}\t{ltLastName[i]:10}\t{ltOVR[i]}\t{ltSPD[i]}\t{ltSTR[i]}\t{ltAGI[i]}\t{ltJMP[i]}\t{ltINJ[i]}\t{ltSTA[i]}")

    ltStats = []
    for i in range(0, len(ltFirstName)):
        ltStats.append([ltFirstName[i], ltLastName[i], ltOVR[i], ltSPD[i], ltSTR[i], ltAGI[i], ltJMP[i], ltINJ[i], ltSTA[i]])

    lt_playerChoice = input("\nPlease enter last name of starting left tackle: ").lower()
    lt_starterChoice = ltDecision(lt_playerChoice)
    roster.append(lt_starterChoice)
    print(f"Great Choice, you picked {lt_starterChoice} as your starting Left Tackle!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Left Guard----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(lgFirstName)):
        print(f"{lgFirstName[i]:10}\t{lgLastName[i]:10}\t{lgOVR[i]}\t{lgSPD[i]}\t{lgSTR[i]}\t{lgAGI[i]}\t{lgJMP[i]}\t{lgINJ[i]}\t{lgSTA[i]}")

    lgStats = []
    for i in range(0, len(lgFirstName)):
        lgStats.append([lgFirstName[i], lgLastName[i], lgOVR[i], lgSPD[i], lgSTR[i], lgAGI[i], lgJMP[i], lgINJ[i], lgSTA[i]])

    lg_playerChoice = input("\nPlease enter last name of starting left guard: ").lower()
    lg_starterChoice = lgDecision(lg_playerChoice)
    roster.append(lg_starterChoice)
    print(f"Great Choice, you picked {lg_starterChoice} as your starting Left Guard!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Center----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(cFirstName)):
        print(f"{cFirstName[i]:10}\t{cLastName[i]:10}\t{cOVR[i]}\t{cSPD[i]}\t{cSTR[i]}\t{cAGI[i]}\t{cJMP[i]}\t{cINJ[i]}\t{cSTA[i]}")

    cStats = []
    for i in range(0, len(cFirstName)):
        cStats.append([cFirstName[i], cLastName[i], cOVR[i], cSPD[i], cSTR[i], cAGI[i], cJMP[i], cINJ[i], cSTA[i]])

    c_playerChoice = input("\nPlease enter first and last name of starting center: ").lower()
    c_starterChoice = cDecision(c_playerChoice)
    roster.append(c_starterChoice)
    print(f"Great Choice, you picked {c_starterChoice} as your starting Center!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Halfback----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(hbFirstName)):
        print(f"{hbFirstName[i]:10}\t{hbLastName[i]:10}\t{hbOVR[i]}\t{hbSPD[i]}\t{hbSTR[i]}\t{hbAGI[i]}\t{hbJMP[i]}\t{hbINJ[i]}\t{hbSTA[i]}")

    hbStats = []
    for i in range(0, len(hbFirstName)):
        hbStats.append([hbFirstName[i], hbLastName[i], hbOVR[i], hbSPD[i], hbSTR[i], hbAGI[i], hbJMP[i], hbINJ[i], hbSTA[i]])

    hb_playerChoice = input("\nPlease enter last name of starting halfback: ").lower()
    hb_starterChoice = hbDecision(hb_playerChoice)
    roster.append(hb_starterChoice)
    print(f"Great Choice, you picked {hb_starterChoice} as your starting Halfback!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    #Pick your Wide Receiver----------
    print(f"\n{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(wrFirstName)):
        print(f"{wrFirstName[i]:10}\t{wrLastName[i]:10}\t{wrOVR[i]}\t{wrSPD[i]}\t{wrSTR[i]}\t{wrAGI[i]}\t{wrJMP[i]}\t{wrINJ[i]}\t{wrSTA[i]}")

    wrStats = []
    for i in range(0, len(wrFirstName)):
        wrStats.append([wrFirstName[i], wrLastName[i], wrOVR[i], wrSPD[i], wrSTR[i], wrAGI[i], wrJMP[i], wrINJ[i], wrSTA[i]])

    wr_playerChoice = input("\nPlease enter last name of starting wide receiver: ").lower()
    wr_starterChoice = wrDecision(wr_playerChoice)
    roster.append(wr_starterChoice)
    print(f"Great Choice, you picked {wr_starterChoice} as your starting Wide Receiver!")

    time.sleep(2)
    clear_terminal()
    #-------------------------------

    roster_str = ', '.join(roster)
    print(f"You're starting roster is {roster_str}")
    print(f"\nThank you for using our generator {name}")

    generate = input("\nWould you like to generate a starting line-up? [y/n]: ").lower()

    while generate != "y" and generate != "n":
        print("INVALID INPUT")
        generate = input("Would you like to generate a starting line-up?: ").lower()