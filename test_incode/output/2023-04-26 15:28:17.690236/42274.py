#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input())
        if words:
            break
    print(words)
    
<|/ file source=github |>