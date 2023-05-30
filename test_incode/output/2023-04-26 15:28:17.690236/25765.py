#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and returns a list of words. """    
    numbers = range(1,10)
    words = []
    
    while True:
        words.append(str(numbers.pop()))
        
        if numbers:
            words.append('