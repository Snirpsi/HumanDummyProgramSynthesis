#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number == 999:
            break
        else:
            numbers.append(number)
    print(numbers)

