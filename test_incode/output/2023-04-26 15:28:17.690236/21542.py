#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and calculates words. """    
    
    numbers = range(1,10)
    
    words = []
    
    for number in numbers:
        words.append(str(number))
        
    print(words)
    
