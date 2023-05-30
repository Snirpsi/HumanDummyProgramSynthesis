#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    
    while True:
        number = input('Enter a number: ')
        
        try:
            number = int(number)
        except ValueError:
            print('That was not a valid number. Try again.')
            continue
        
        numbers.append(number)
        
        print('The number', number, 'is', sum(numbers))
        
        print('-' * 50)
        
        print('Enter a number again:')
        
