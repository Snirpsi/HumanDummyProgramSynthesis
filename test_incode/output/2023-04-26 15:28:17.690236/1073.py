#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = []
    for _ in range(int(input('Enter a number: '))):
        numbers.append(int(input('Enter a number: ')))
    print('The list contains:')
    for number in numbers:
        print(number)
    print('The list contains:')
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print(number, 'is odd')
    print('The list contains:')
    for number in numbers:
        if number % 3 == 0:
            print(number, 'is even')
        else:
            print(number, 'is prime')
    print('The list contains:')
    for number in numbers:
        if number % 5 == 0:
            print(number, 'is divisible by 5')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 7 == 0:
            print(number, 'is divisible by 7')
        else:
            print(number, 'is divisible by 5')
    print('The list contains:')
    for number in numbers:
        if number % 11 == 0:
            print(number, 'is divisible by 11')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 13 == 0:
            print(number, 'is divisible by 13')
        else:
            print(number, 'is divisible by 5')
    print('The list contains:')
    for number in numbers:
        if number % 17 == 0:
            print(number, 'is divisible by 17')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 19 == 0:
            print(number, 'is divisible by 19')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 23 == 0:
            print(number, 'is divisible by 23')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 29 == 0:
            print(number, 'is divisible by 29')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 31 == 0:
            print(number, 'is divisible by 31')
        else:
            print(number, 'is divisible by 3')
    print('The list contains:')
    for number in numbers:
        if number % 37 == 0:
            print(number, 'is divisible by 37')
        else:
            print(number, 'is divisible by 3')
    print('