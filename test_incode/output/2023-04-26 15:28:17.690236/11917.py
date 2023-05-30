#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        words.append(line.strip())
    
    words = map(int, words)
    
    product = 1
    
    for word in words:
        product *= word
    
    print(product)

<|/ file ext=.py source=github |>