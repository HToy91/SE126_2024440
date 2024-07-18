#Jose Vargas Figueroa
#SE126 Lab 1
#07/17/2024

#Program Prompt: determine whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.

#----------FUNCTIONS----------
#Part 1
def difference(people, max_cap):
    '''a function that is passed both the number of people attending the meeting, as well as the
maximum room capacity. This function determines the number of people over/under the
capacity based on these two values, and return the difference value.'''
    diff = max_cap - people

    return diff

#Part 2
def decision(response):
    '''a function that is passed a value that represents ‘response’: the user’s response to whether or not they would like to continue in the program and enter another meeting’s attendance information. The function checks this value and ensure it is either a lowercase ‘y’ or ‘n’. When the value is not either of these appropriate valid values, trap the user in a loop and repeatedly ask them to re-enter a valid value (‘y’ or ‘n’) until they have. Once the user has supplied one of the two valid values, return said value from the function.'''
    while response.lower() != "y" and response.lower() != "n":
        print("****INVALID ENTRY*****")
        response = input("Would you like to continue in the program and enter another meeting’s attendance information.[y/n]: ")

    return response

#Part 3
#----------MAIN CODE----------
ans = "y"

while ans == "y":#start of loop
    try:#makes sure proper values are entered for variables
        meetingName = input("Plese enter name of meeting: ")
        max_cap = int(input("What is the room capacity?: "))
        people = int(input("How many people are attending?: "))
        peopleDiff = int(difference(people, max_cap))#passes the function 

        if people <= max_cap:
            print(f'\nThe meeting "{meetingName}" meets fire safety regulations')
            print(f"You are still able to add {peopleDiff} people to the room and meet fire regulations")

        else:
            print(f'\n*****Meeeting "{meetingName}" DOES NOT meet fire safety regulations!*****')
            print(f'\nYou must remove {abs(peopleDiff)} people from the meeting "{meetingName}"')#abs is absolute value so negative number comes out as distance from 0

        question = input("\nWould you like to continue in the program and enter another meeting’s attendance information.[y/n]: ")
        ans = decision(question).lower()#input for question runs through the function and passes to ans so it can restart or end loop

    except ValueError: #if a ValueError comes up, it goes back to try:
        print("\n*****INVALID ENTRY*****")

print("\nThank You, Goodbye!")