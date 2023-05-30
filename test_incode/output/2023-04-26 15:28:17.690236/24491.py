#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and converts user input. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
            continue
        else:
            break
    
    numbers = sorted(numbers)
    
    print('The sorted numbers are: ', numbers)
    
