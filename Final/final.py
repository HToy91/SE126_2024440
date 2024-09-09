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
    print("2. Add/Delete Contact")
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
        print("2. Add/Delete Contact")
        print("3. Quit")

        mChoice = input("\nEnter Menu Option[1-3]: ")

    return mChoice

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

        print("Add/Delete")
        print("--------------------")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Main Menu")

        addDelChoice = input("\nEnter Menu Option[1-3]: ")

    return addDelChoice

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
                print(f"{add_name} Added!")
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
                while del_question not in {"y","n"}:
                    print("INVALID INPUT")
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()

                    del_question = input("Are you sure[y/n]: ").lower()

                if del_question == "y":
                    print(f"{del_name} DELETED")
                    contacts.remove(del_name)
                    del phoneBook[f"{del_name}"]
                    time.sleep(2)#delays clearing terminal
                    clear_terminal()

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