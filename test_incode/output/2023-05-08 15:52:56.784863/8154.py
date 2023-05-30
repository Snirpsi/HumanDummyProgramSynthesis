#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The program will keep running until the user enters 0.
    while True:
        number = input("Enter a number: ")
        if number == '0':
            break
        else:
            numbers.append(int(number))
    print(numbers)

