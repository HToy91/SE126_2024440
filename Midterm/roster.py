#Jose Vargas Figueroa
#SE126 Midterm
#08/13/2024

#Program Prompt:

import random
import csv

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

#def qbChoice():


print("Welcome to the Patriots starting line-up generator!")

generate = input("Would you like to generate a starting line-up? [y/n]: ").lower()

while generate != "y" and generate != "n":
    print("INVALID INPUT")
    generate = input("Would you like to generate a starting line-up?: ").lower()

while generate == "y":
    name = input("\nPlease enter your name: ")
    print(f"Welcome {name}!")

    print(f"{'FIRST NAME':10}\t{'LAST NAME':10}\t{'OVR'}\t{'SPD'}\t{'STR'}\t{'AGI'}\t{'JMP'}\t{'INJ'}\t{'STA'}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range (0, len(qbFirstName)):
        print(f"{qbFirstName[i]:10}\t{qbLastName[i]:10}\t{qbOVR[i]}\t{qbSPD[i]}\t{qbSTR[i]}\t{qbAGI[i]}\t{qbJMP[i]}\t{qbINJ[i]}\t{qbSTA[i]}")

    qbStats = []
    for i in range(0, len(qbFirstName)):
        qbStats.append([qbFirstName[i], qbLastName[i], qbOVR[i], qbSPD[i], qbSTR[i], qbAGI[i], qbJMP[i], qbINJ[i], qbSTA[i]])

    qbChoice = []
    input("Please enter last name of starting quarterback: ").lower()

    if input == "maye":
        qbChoice.append(qbFirstName[0], qbLastName[0])

    print(qbChoice)