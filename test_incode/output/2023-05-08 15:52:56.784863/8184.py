#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The program will keep on looping until the user enters 0.
    #The program will then print the list.
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(numbers)
            numbers.append(number)
    print(numbers)

