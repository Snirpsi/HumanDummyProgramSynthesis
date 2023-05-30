#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    #The function will stop when the user enters a number greater than 9
    #The function will then print out the numbers in the list
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if number > 9:
            break
        numbers.append(number)
    print(numbers)

