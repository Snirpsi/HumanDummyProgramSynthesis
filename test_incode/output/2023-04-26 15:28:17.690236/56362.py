#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and iterates over user input. """    
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input. Try again.')
            continue
        
        if len(numbers) == 