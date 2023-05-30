#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    return words

<|/ file filename=word