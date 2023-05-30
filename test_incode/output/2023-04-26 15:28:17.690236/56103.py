#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers and removes user input. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
            continue
        
        if len(numbers) == 0:
            break
        
    print('The numbers are:')
    
    for number in numbers:
        print(number)
    
    print('\nThe numbers were:')
    
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 3 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 5 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 7 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 11 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 13 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 17 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 19 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 23 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 29 == 0:
            print(number)
        else:
            print('Not a prime')
    
    print('\nThe numbers that do not have a prime factor')
    
    for number in numbers:
        if number % 31 == 0:
            print(number)
        else:
            print('