#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that adds a list of numbers.
    #The program will exit when the user presses Ctrl+C
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == numbers[-2]:
            break
    print(numbers)

