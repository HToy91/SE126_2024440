#W1D2 SE116 Review Demo - split into parts in Canvas

#Jose Vargas Figueroa [YOUR NAME]
#Lab # or Demo Title
#July 17th [W1D2] - 

#PROGRAM PROMPT: this is tempF to tempC conversion program that averages all temps entered

#VARIABLE DICTIONARY


#----------FUNCTIONS----------
def converter(f):

    '''this function is passed a temp F value, converts to C, and returns said value'''
    c = (f - 32) * (5 / 9)

    return c #literally returns to the point of function call

#----------MAIN CODE----------

#initializing known or needed values
tempCount = 0
tempSum = 0

degree = u'\N{DEGREE SIGN}'

answer = "y"

while answer.lower() == "y" or answer.lower() == "yes":

    tempF = float(input(f"\t\tEnter temperature #{tempCount + 1} in Fahrenheit: "))

    tempCount += 1 #tempCount = tempCount + 1
    tempSum += tempF #tempSum = tempSum + tempF

#convert F to C --> use function which returns a value
    #tempC = (tempF - 32) * (5 / 9)

    tempC = converter(tempF)

    print(f"\tTemperature: {tempF:.1f}{degree}F   |   {tempC:.1f}{degree}C")


    #build a way out!
    answer = input("\t\tWould you like to enter another temp? [y/n]: ")

    #error trap
    while answer.lower() != "y" and answer.lower() != "n" and answer.lower() != "yes" and answer.lower() != "no":
        print("\t\t***INVALID ENTRY***")
        answer = input("\t\tWould you like to enter another temp? [y/n] ")

if tempCount != 0:
    avgTemp = tempSum / tempCount
    avgC = converter(avgTemp)

    print(f"\n\nYou have entered {tempCount} temperatures for an average of {avgTemp:.1f}F  |   {avgC:.1f}{degree}C")

    print("\n\n\tThank you & GOodbye.\n\n")

else:
    print("\n\n\tOkay, goodbye!\n\n")