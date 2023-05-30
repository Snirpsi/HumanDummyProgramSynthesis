#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The program will exit when the user enters a number that is
    #not in the list.
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            print("That number is not in the list")
        else:
            numbers.append(number)
            break
    #The program will exit when the user enters the number 9.
    if number == 9:
        print("Thank you for using the program")
    else:
        print("That number is not in the list")

