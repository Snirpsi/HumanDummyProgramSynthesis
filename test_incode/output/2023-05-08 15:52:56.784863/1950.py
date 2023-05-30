#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The program will keep looping until the user enters stop.
    while True:
        number = input("Enter a number: ")
        if number == 'stop':
            break
        else:
            numbers.append(number)
    print(numbers)

