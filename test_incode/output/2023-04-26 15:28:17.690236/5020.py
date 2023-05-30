#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or iterates over a list of numbers. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input. Try again.')
            continue
        
        if len(numbers) == 