#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and returns a list of words. """    
    
    numbers = [int(i) for i in input().split()]
    
    words = [str(number) for number in numbers]
    
    print(" ".join(words))
    
