#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The program will stop when the user enters 0.
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            numbers.append(number)
    print(numbers)

