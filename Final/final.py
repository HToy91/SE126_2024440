#Jose Vargas Figueroa
#SE126 Final
#09/11/2024

#Program Prompt: I will create a program that is basically a phone book. The user will be able to select from three options in the main menu: view contacts, add or delete contact, or quit the program. When the user selects the view contacts option, they will be shown all their contacts in a phone book dictionary and the list will be sorted. They will then be able to type in a name in the list and be able to view the phone number attached. If they select the add or delete option, they then will be asked if they want to add or delete a contact. If “add” is chosen they will be able to enter the name they want to add, enter a phone number, and it will be added to the phone book. If “delete” is chosen, then they will be able to enter the name of the contact they want to delete, and it will be deleted from the phone book. The third menu option just ends the program.

import csv
import os
import time

#Dictionary containing initial contacts and their phone numbers
phoneBook = {
    "jose": "(508) 717-1249",
    "james": "(401) 284-5632",
    "matt": "(774) 862-5734",
    "luis": "(508) 868-9283",
    "stephanie": "(774) 928-8972",
    "andrew": "(508) 824-2193"
}

#Lists to store names and numbers separately
contacts = []
numbers = []

#Function to save contacts to a CSV file
def saveContacts():
    with open("Final/phonebook.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        for name, number in phoneBook.items():
            writer.writerow([name, number])

#Function to load contacts from the CSV file
def loadContacts():
    global phoneBook
    #Checks if the CSV file exists before attempting to read it
    if os.path.exists("Final/phonebook.csv"):
        with open("Final/phonebook.csv", "r") as file:
            reader = csv.reader(file)
            phoneBook.clear()#Clears current phoneBook to avoid duplication
            for row in reader:
                if row:
                    phoneBook[row[0]] = row[1]#Adds contact to te phoneBook
            #Clears contacts and numbers lists with updated phoneBook data
            contacts.clear()
            numbers.clear()
            #Populates contacts and numbers lists with updated phoneBook data
            for key, value in phoneBook.items():
                contacts.append(key)
                numbers.append(value)

#Function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to display main menu
def menu():
    print("PHONE BOOK")
    print("--------------------")
    print("1. Contacts")#option for full list or search
    print("2. Add/Delete Contact")
    print("3. Quit")

    #Input validation
    mChoice = input("\nEnter Menu Option[1-3]: ")
    if mChoice not in {"1","2","3"}:
        time.sleep(1)
        clear_terminal()

        print("INVALID INPUT")
        time.sleep(1)
        clear_terminal()

        return menu()

    return mChoice

#Function to display the ADD/Delete submenu
def addDel_menu():
    print("Add/Delete")
    print("--------------------")
    print("1. Add Contact")#option for full list or search
    print("2. Delete Contact")
    print("3. Main Menu")

    addDelChoice = input("\nEnter Menu Option[1-3]: ")

    if addDelChoice not in {"1","2","3"}:
        time.sleep(1)
        clear_terminal()

        print("INVALID INPUT")
        time.sleep(1)
        clear_terminal()

        return addDel_menu()

    return addDelChoice



answer = "y"

#initial population of contacts and numbers lists based on phoneBook
for key in phoneBook:
            #print(key)
            contacts.append(key)
            numbers.append(phoneBook[key])

#Loads contacts from CSV file if any exists
loadContacts()

#Main loop
while answer.lower() == "y":
    menu_choice = menu()
    time.sleep(1)
    clear_terminal()

    #Menu option 1: Displays contacts
    if menu_choice == "1":
        time.sleep(1)
        clear_terminal()

        print("CONTACTS")
        print("--------------------")
        
        #Bubble sort
        for i in range(0, len(contacts) - 1):
            for index in range(0, len(contacts) - 1):
                if (contacts[index] > contacts[index + 1]):
                    temp = contacts[index]
                    contacts[index] = contacts[index + 1]
                    contacts[index + 1] = temp
                    
        for i in range(0, len(contacts)):
            print(contacts[i].upper())

        contactSearch = input("\nEnter Contacts Name: ").lower()
        time.sleep(1)
        clear_terminal()

        #Binary search
        min = 0
        max = len(contacts) - 1
        mid = int((min + max) / 2)

        while (min < max and contactSearch != contacts[mid]):
            if contactSearch < contacts[mid]:
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)
            
        if contactSearch == contacts[mid]:
            print(contactSearch.upper() + ": " + phoneBook[contactSearch])

        else:
            print("Contact not Found")
            time.sleep(1)
            clear_terminal()

        returnMenu = input("\nPress 'ENTER' to return to Main Menu")

        time.sleep(2)#delays clearing terminal
        clear_terminal()

        #checks for invalid input
        while returnMenu != "":
            print("INVALID ENTRY")
            returnMenu = input("\nPress 'ENTER' to return to Main Menu")

            time.sleep(2)#delays clearing terminal
            clear_terminal()
            #else:

    #Menu option 2: Add or delete contacts
    elif menu_choice == "2":
        addDel_menuChoice = addDel_menu()
        time.sleep(2)#delays clearing terminal
        clear_terminal()

        if addDel_menuChoice == "1":
            add_name = input("Enter name to ADD: ").lower()
            if add_name in contacts:
                print("Already in Phone Book")
            else:
                add_num = input("Enter Phone Number[(xxx) xxx-xxxx)]: ")
                contacts.append(add_name)
                phoneBook[f"{add_name}"] = add_num

                saveContacts()#Save updated phoneBook to CSV file

                print(f"{add_name.upper()} Added!")
                time.sleep(2)#delays clearing terminal
                clear_terminal()

        if addDel_menuChoice == "2":
            time.sleep(2)#delays clearing terminal
            clear_terminal()

            del_name = input("Enter name to DELETE: ").lower()
            while del_name not in phoneBook:
                time.sleep(2)#delays clearing terminal
                clear_terminal()
                
                print("Name NOT Found")
                time.sleep(2)#delays clearing terminal
                clear_terminal()

                del_name = input("Enter name to DELETE: ").lower()

            else:
                del_question = input("Are you sure[y/n]: ").lower()
                time.sleep(1)
                clear_terminal()
                
                while del_question not in {"y","n"}:
                    print("INVALID INPUT")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()

                    del_question = input("Are you sure[y/n]: ").lower()

                if del_question == "y":
                    print(f"{del_name.upper()} DELETED")
                    contacts.remove(del_name)
                    del phoneBook[f"{del_name}"]

                    saveContacts()#Save updated phoneBook to CSV file

                    time.sleep(2)#delays clearing terminal
                    clear_terminal()

    #Menu option 3: Quit program
    else:
        quitProgram = input("Are you sure[y/n]: ").lower()
        time.sleep(1)
        clear_terminal()
        if quitProgram not in {"y","n"}:
            print("INVALID ENTRY")
            time.sleep(1)
            clear_terminal()

            quitProgram = input("Are you sure[y/n]: ").lower()

        if quitProgram == "y":
            #exits loop
            answer = "n"#Ends program

        else:
            #continues program
            answer = "y"