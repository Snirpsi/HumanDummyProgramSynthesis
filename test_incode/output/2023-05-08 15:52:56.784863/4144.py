#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers == []:
            break
    print(numbers)

