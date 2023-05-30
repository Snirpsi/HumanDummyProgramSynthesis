#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that iterates over a list of numbers.
    #The loop will terminate when the user enters a number that is
    #not in the list.
    while True:
        number = input("Enter a number between 1 and 9: ")
        if number not in numbers:
            print("That number is not in the list")
        else:
            print(number)
            break

