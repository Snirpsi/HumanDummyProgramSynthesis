#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    #The loop will stop when numbers is empty
    numbers = []
    while numbers:
        numbers.append(int(input('Enter a number: ')))
    print(numbers)

