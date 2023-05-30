#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and iterates over user input. """    
    
    numbers = input('Enter numbers: ')
    
    numbers = [int(n) for n in numbers.split()]
    
    for n in numbers:
        print(n)
        
    print('Done')
    
