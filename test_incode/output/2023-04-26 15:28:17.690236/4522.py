#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    
    words = []
    
    for _ in range(int(input())):
        words.append(input())
    
    words.sort()
    
    print(" ".join(words))
    
