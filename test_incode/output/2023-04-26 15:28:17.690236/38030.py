#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers and stores words. """    
    
    numbers = [int(n) for n in input().split()]
    
    words = []
    
    for n in numbers:
        words.append(str(n))
        
    print(" ".join(words))
    
