#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that stores numbers.
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            print(number)
        else:
            print("That number is not in the list")
            break

