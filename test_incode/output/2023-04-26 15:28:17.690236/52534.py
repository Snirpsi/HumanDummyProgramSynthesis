#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and enumerates numbers. """    
    numbers = [int(x) for x in input('Enter a number: ').split()]
    
    numbers_enumerated = enumerate(numbers)
    
    for number, enumerated_number in numbers_enumerated:
        print(number, enumerated_number)
        
