#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    return words

<|/ file source=github |>