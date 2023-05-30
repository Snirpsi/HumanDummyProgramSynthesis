#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and stores a list of words. """    
    words = []
    
    for _ in range(int(input())):
        words.append(input())
    
    print(" ".join(words))
    
