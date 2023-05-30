#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and enumerates numbers. """    
    while True:
        number = int(input('Enter a number: '))
        number *= number
        print(number, end='\t')
        
        if number == 