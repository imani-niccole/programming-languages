# Programming Languages | Python Menus + Functions
# Imani Candler | 9.1.2024
# Objective: Using menus & functions to calculate the area and perimeter of user's chosen shape
import math
# functions below
def menu():
    print("1. Rectangle")
    print("2. Circle")
    print("3. Hexagon")
    print("4. Pentagon")
    print("5. Quit, exit program!")

def option1():
    rlength = float(input("Please enter the length: "))
    rwidth = float(input("Please enter the width: "))
    print ()
    rarea = rlength * rwidth
    rperimeter = (rlength * 2) + (rwidth * 2)
    print()
    print ("Your rectangle's area is: ", rarea)
    print ("Your rectangle's perimeter is: ", rperimeter)

def option2():
    cradius = float(input("Please enter the radius: "))
    carea = math.pi * (cradius ** 2) # radius is squared
    circumference = 2 * math.pi * cradius
    print()
    print ("Your circle's area is: ", cradius)
    print ("Your circle's circumference is: ", circumference)

def option3():
    hlength = float(input("Please enter length: "))
    harea = ((3*(math.sqrt(3)))/2) * (hlength ** 2) #area of hexagon
    hperimeter = 6 * hlength
    print()
    print ("Your hexagon's area is: ", harea)
    print ("Your hexagon's perimeter is: ", hperimeter)

def option4():
    plength = float(input("Please enter the pentagon's length: "))
    parea = 0.25 * (math.sqrt(5 * (5 + 2 * (math.sqrt(5))))) * (6 ** 2) # pentagon area
    pperimeter = 5 * plength
    print()
    print ("Your pentagon's area is: ", parea)
    print ("Your pentagon's perimeter is: ", pperimeter)

##############################################

print ("Hi, look at the menu!")
print()
menu()
print()
option = int(input("Enter your option: "))
print()

while option != 5:
    if option == 1:
        print ("You chose the rectangle!")
        option1() # calls functions from above

    elif option == 2:
        print ("You chose the circle!")
        option2()

    elif option == 3:
        print ("You chose the hexagon!")
        option3()

    elif option == 4:
        print("You chose the pentagon!")
        option4()

    else:
        print("Invalid option! Enter a different number: ")
    print()
    menu()
    print()
    option = int(input("Enter your option: "))


print()
print("THANK YOU GOODBYE") # exits the menu loop, program is finished!