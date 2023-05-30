#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and enumerates words. """    
    
    words = []
    
    for _ in range(int(input())):
        words.append(input())
        
    words.sort()
    
    for word in words:
        print(word)
        
