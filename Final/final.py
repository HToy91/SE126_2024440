import os
import time

phoneBook = {
    "jose": "(508) 717-1249",
    "james": "(401) 284-5632",
    "matt": "(774) 862-5734",
    "luis": "(508) 868-9283",
    "stephanie": "(774) 928-8972",
    "andrew": "(508) 824-2193"
}

contacts = []
numbers = []

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("PHONE BOOK")
    print("--------------------")
    print("1. Contacts")#option for full list or search
    print("2. Add Contact")
    print("3. Quit")

    mChoice = input("\nEnter Menu Option[1-3]: ")
    if mChoice not in {"1","2","3"}:
        time.sleep(1)
        clear_terminal()

        print("INVALID INPUT")
        time.sleep(1)
        clear_terminal()

        print("PHONE BOOK")
        print("--------------------")
        print("1. Contacts")#option for full list or search
        print("2. Add Contact")
        print("3. Quit")

        mChoice = input("\nEnter Menu Option[1-3]: ")

    return mChoice

answer = "y"
for key in phoneBook:
            #print(key)
            contacts.append(key)
            numbers.append(phoneBook[key])

while answer.lower() == "y":
    menu_choice = menu()
    time.sleep(1)
    clear_terminal()

    if menu_choice == "1":
        time.sleep(1)
        clear_terminal()

        print("CONTACTS")
        print("--------------------")
        
        for i in range(0, len(contacts) - 1):
            for index in range(0, len(contacts) - 1):
                if (contacts[index] > contacts[index + 1]):
                    temp = contacts[index]
                    contacts[index] = contacts[index + 1]
                    contacts[index + 1] = temp
                    
        for i in range(0, len(contacts)):
            print(contacts[i])

        contactSearch = input("\nEnter Contacts Name: ").lower()
        time.sleep(1)
        clear_terminal()

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
            print(contactSearch + ": " + phoneBook[contactSearch])

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

    #elif menu_choice == "2":

    '''else:
        quitProgram = input("Are you sure[y/n]: ").lower()
        if quitProgram not in {"y","n"}:
            print("INVALID ENTRY")
            quitProgram = input("Are you sure[y/n]: ").lower()

        if quitProgram == "y":
            #exits loop
            answer = "n"

        else:
            #continues program
            answer = "y"'''