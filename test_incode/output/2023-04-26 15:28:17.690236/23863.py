#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    i = 0
    while i < len(words):
        words[i] = words[i] * 2
        i += 1
    
    print(words)
    
