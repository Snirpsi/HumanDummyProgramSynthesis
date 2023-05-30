#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that requests a list of numbers.
    while True:
        numbers = input("Enter a number: ")
        try:
            number = int(numbers)
        except ValueError:
            print("Invalid number")
        else:
            print(numbers)
            break

