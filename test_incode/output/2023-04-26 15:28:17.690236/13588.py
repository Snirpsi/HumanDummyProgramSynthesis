#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and prints words. """    
    words = []
    while True:
        words.append(input())
        if words[-1] == 'q':
            break
    
    print(words)
    
