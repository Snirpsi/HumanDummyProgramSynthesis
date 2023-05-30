#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and calculates a list of numbers. """    
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 0:
            print('Negative numbers are not allowed')
            continue
        
        if number == 0:
            print('Zero is not allowed')
            continue
        
        if number % 2 == 0:
            print('Only even numbers are allowed')
            continue
        
        if number % 3 == 0:
            print('Only odd numbers are allowed')
            continue
        
        print('The list contains:')
        
        numbers = []
        
        for i in range(number):
            numbers.append(i)
        
        print(' '.join(map(str, numbers)))
        
        print('Would you like to enter another number? (Y/N)')
        
        choice = input('> ')
        
        if choice == 'Y':
            continue
        
        if choice == 'N':
            break
        
        print('Invalid input')
        
    print('Goodbye!')
    
