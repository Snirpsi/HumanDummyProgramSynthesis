#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The program will keep running until the user enters 0.
    #The program will then print out the list.
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == 0:
            break
    print(numbers)

