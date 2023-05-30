#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    for number in numbers:
        print(number)
        number = input("Enter a number: ")
        #A loop that prints the number the user entered.
        while number != "":
            print(number)
            number = input("Enter a number: ")
            #A loop that prints the number the user entered.

