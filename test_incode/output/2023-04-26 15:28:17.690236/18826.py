#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = input('Enter a list of numbers: ')
    numbers = numbers.split()
    
    numbers = [int(number) for number in numbers]
    
    numbers_converted = []
    
    for number in numbers:
        numbers_converted.append(number * 2)
    
    print('The list converted is:', numbers_converted)
    
