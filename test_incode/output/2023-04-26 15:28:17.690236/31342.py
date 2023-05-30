#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and prints words. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    words = []
    for number in numbers:
        words.append(str(number))
    
    print('\n'.join(words))
    
