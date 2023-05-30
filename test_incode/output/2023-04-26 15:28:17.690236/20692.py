#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and returns words. """    
    
    numbers = [int(i) for i in input().split()]
    
    words = []
    
    for num in numbers:
        words.append(str(num))
    
    print(" ".join(words))
    
