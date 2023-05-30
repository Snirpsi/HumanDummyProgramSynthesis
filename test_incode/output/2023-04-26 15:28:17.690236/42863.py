#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    
    numbers = open('numbers.txt','r')
    
    for number in numbers:
        print(number)
        
    numbers.close()
    
