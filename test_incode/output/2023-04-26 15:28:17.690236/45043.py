#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers. """    
    numbers = open('numbers.txt', 'r')
    
    for number in numbers:
        print(number.rstrip())
        
    numbers.close()
    
