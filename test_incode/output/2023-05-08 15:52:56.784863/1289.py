#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    #This program will keep looping until the user enters 0.
    #The program will then print the list.
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            numbers.append(number)
    print(numbers)

