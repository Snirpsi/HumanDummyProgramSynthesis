#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    return words

<|/ file filename=words.py ext=.py |>