#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    numbers = []
    while numbers:
        number = input("Enter a number: ")
        if number in numbers:
            numbers.remove(number)
        else:
            print("That number is not in the list")

