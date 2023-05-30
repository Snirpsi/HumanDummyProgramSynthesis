#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or returns words. """    
    
    words = []
    
    while True:
        words.append(input())
        
        if words[-1] == 'q':
            break
        
    return words

<|/ file ext=.py source=github |>