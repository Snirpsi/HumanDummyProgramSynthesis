#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that converts numbers.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print(number, "is a prime number")
            break
        else:
            print("That is not a prime number")

