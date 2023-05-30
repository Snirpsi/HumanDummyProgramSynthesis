#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    #The program will keep running until the user enters 0.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            numbers.remove(number)
        else:
            break
    print(numbers)

