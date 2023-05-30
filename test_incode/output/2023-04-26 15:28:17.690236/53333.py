#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and calculates words. """    
    
    numbers = range(10)
    
    for number in numbers:
        word = ''.join(str(number))
        print(word)
    
