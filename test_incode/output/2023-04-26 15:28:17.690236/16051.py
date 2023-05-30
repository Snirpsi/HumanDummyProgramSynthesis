#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        print('Current number:', numbers.pop(0))
        
        if numbers:
            print('Next number:', numbers.pop(0))
        else:
            print('End of list')
        
