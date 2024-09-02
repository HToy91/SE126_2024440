#Jose Vargas Figueroa
#SE126 Lab 5 Individual sequential and binary search
#09/01/2024

#Program Prompt: In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file below. You will perform both sequential search as well as binary search. See the lab prompt for further details. 

import csv

#variables
#Lists to store student data
id_student = []
lName = []
fName = []
class1 = []
class2 = []
class3 =[]
#mChoice = input("Please select a Menu Option[1-5]: ")
#menu_choice = menu()
#min = 0
#max = len(id_student) - 1
#mid = int((min + max) / 2)
#search_ID = input("Pleas enter Student ID: ")
#found = -1
#search_class = input("Please enter Class Name: ").lower()
#quitProgram = input("Are you sure[y/n]: ").lower()

#open and read csv file
with open ("Labs/lab5Individual/lab5_students.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        id_student.append(rec[0])
        lName.append(rec[1])
        fName.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
#disconnect from csv----------

#function to display menu
def menu():
    print("~MENU~")
    print("--------------")
    print("\n1. See All Student Report")
    print("2. Search for a Student[ID]")
    print("3. Search for Student[Last]")
    print("4. View a class Roster [class1, class2, class3]")
    print("5. Exit/Quit Program")

    mChoice = input("\nPlease select a Menu Option[1-5]: ")
    if mChoice not in {"1","2","3","4","5"}:
        print("INVALID ENTRY")
        mChoice = input("Please select a Menu Option[1-5]: ")
    
    return mChoice

#Main Program Loop
answer = "y"

while answer.lower() == "y":
    #displays menu and returns user's choice
    menu_choice = menu()

    #option 1 displays all student info
    if menu_choice == "1":
        print(f"{"ID":15} {"LastName":15} {"FirstName":15} {"Class1":15} {"Class2":15} {"Class3"}")
        print("-----------------------------------------------------------------------------------------")
        for i in range(0, len(id_student)):
            print(f"{id_student[i]:15} {lName[i]:15} {fName[i]:15} {class1[i]:15} {class2[i]:15} {class3[i]}")
        print("\n")

    #option 2 searches for a student by ID using binary search
    elif menu_choice == "2":
        min = 0
        max = len(id_student) - 1
        mid = int((min + max) / 2)

        search_ID = input("Pleas enter Student ID: ")

        while (min < max and search_ID != id_student[mid]):
            if search_ID < id_student[mid]:
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min +max) / 2)

        if search_ID == id_student[mid]:
            print(f"\nID {search_ID} found!")
            print(f"{lName[mid]}, {fName[mid]}\n\nClasses:\n\t{class1[mid]}\n\t{class2[mid]}\n\t{class3[mid]}\n")

        else:
            print(f"{search_ID} NOT FOUND\n")
        
    #option 3 searches for a student by last name using binary search    
    elif menu_choice == "3":
        min = 0
        max = len(lName) - 1
        mid = int((min + max) / 2)

        search_lName = input("Please enter Student's last name: ").lower()

        while (min < max and search_lName != lName[mid].lower()):
            if search_lName < lName[mid].lower():
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min +max) / 2)

        if search_lName == lName[mid].lower():
            print(f"\nLast Name {search_lName} found!")
            print(f"{lName[mid]}, {fName[mid]}\n\nClasses:\n\t{class1[mid]}\n\t{class2[mid]}\n\t{class3[mid]}\n")

        else:
            print(f"{search_lName} NOT FOUND\n")

    #option 4 views a class roster
    elif menu_choice == "4":
        found = -1
        search_class = input("Please enter Class Name: ").lower()
        print(f"{"ID":15} {"LastName":15} {"FirstName":15}")
        print("----------------------------------------------")
        #checks for searched class and prints the students in that class
        for i in range(0, len(fName)):
            if search_class == class1[i].lower() or search_class == class2[i].lower() or search_class == class3[i].lower():
                found = i           
                print(f"{id_student[found]:15} {lName[found]:15} {fName[found]:15}")

        if found == -1:
            print("CLASS DOES NOT EXIST")
        print("\n")

    #option 5 exits the program
    else:
        quitProgram = input("Are you sure[y/n]: ").lower()
        if quitProgram not in {"y","n"}:
            print("INVALID ENTRY")
            quitProgram = input("Are you sure[y/n]: ").lower()

        if quitProgram == "y":
            #exits loop
            answer = "n"

        else:
            #continues program
            answer = "y"