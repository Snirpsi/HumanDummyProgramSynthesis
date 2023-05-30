#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The program will keep running until the user exits.
    while True:
        print(numbers)
        numbers = input("Enter a number: ")
        if numbers == 'q':
            break
        else:
            numbers.append(int(numbers))

