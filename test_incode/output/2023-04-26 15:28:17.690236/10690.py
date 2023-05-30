#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    for _ in range(int(input())):
        words.append(input().split())
    
    words.sort()
    
    for word in words:
        print(word)
        
