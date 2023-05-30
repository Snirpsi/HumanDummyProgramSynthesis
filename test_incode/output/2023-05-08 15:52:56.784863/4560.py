#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that requests numbers.
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            print("Number found!")
            break
        else:
            print("Number not found!")

