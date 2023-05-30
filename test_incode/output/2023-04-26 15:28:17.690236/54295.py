#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and converts a list of words. """    
    
    numbers = [int(i) for i in input().split()]
    
    words = []
    
    for number in numbers:
        words.append(str(number))
        
    words.sort()
    
    print(" ".join(words))
    
