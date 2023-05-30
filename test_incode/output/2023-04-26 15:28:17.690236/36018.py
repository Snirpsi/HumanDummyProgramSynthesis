#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and iterates over a list of numbers. """    
    
    # Read a text file containing numbers
    numbers = open('numbers.txt').read().splitlines()
    
    # Remove all numbers from list
    numbers = [x for x in numbers if x != '']
    
    # Iterate over numbers
    for number in numbers:
        # Remove all non-digit characters from number
        number = number.replace('.', '')
        
        # Remove all non-digit characters from number
        number = number.replace('-', '')
        
        # Remove all non-digit characters from number
        number = number.replace('/', '')
        
        # Remove all non-digit characters from number
        number = number.replace('+', '')
        
        # Remove all non-digit characters from number
        number = number.replace(',', '')
        
        # Remove all non-digit characters from number
        number = number.replace(';', '')
        
        # Remove all non-digit characters from number
        number = number.replace('?', '')
        
        # Remove all non-digit characters from number
        number = number.replace('!', '')
        
        # Remove all non-digit characters from number
        number = number.replace('\'', '')
        
        # Remove all non-digit characters from number
        number = number.replace('(', '')
        
        # Remove all non-digit characters from number
        number = number.replace(')', '')
        
        # Remove all non-digit characters from number
        number = number.replace(',', '')
        
        # Remove all non-digit characters from number
        number = number.replace(';', '')
        
        # Remove all non-digit characters from number
        number = number.replace('?', '')
        
        # Remove all non-digit characters from number
        number = number.replace('!', '')
        
        # Remove all non-digit characters from number
        number = number.replace('\'', '')
        
        # Remove all non-digit characters from number
        number = number.replace('(', '')
        
        # Remove all non-digit characters from number
        number = number.replace(')', '')
        
        # Remove all non-digit characters from number
        number = number.replace(',', '')
        
        # Remove all non-digit characters from number
        number = number.replace(';', '')
        
        # Remove all non-digit characters from number
        number = number.replace('?', '')
        
        # Remove all non-digit characters from number
        number = number.replace('!', '')
        
        # Remove all non-digit characters from number
        number = number.replace('\'', '')
        
        # Remove all non-digit characters from number
        number = number.replace('(', '')
        
        # Remove all non-digit characters from number
        number = number.replace(')', '')
        
        # Remove all non-digit characters from number
