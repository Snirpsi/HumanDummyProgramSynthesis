#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers and iterates over words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        number = int(word)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number * 2)
        
        print('\n')
    
