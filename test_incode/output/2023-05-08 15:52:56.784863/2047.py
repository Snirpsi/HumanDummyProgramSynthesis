#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print(number)
        else:
            print("That number is not in the list")
            break

