#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['hello', 'world', 'python', 'is', 'a', 'cool', 'program']
    
    i = 0
    while i < len(words):
        print('#', end='')
        for word in words:
            print(' ', end='')
            print(word, end='')
        print('\n')
        i += 1
        
