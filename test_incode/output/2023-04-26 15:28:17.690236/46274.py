#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        words.append(line)
    print(' '.join(words))

<|/ file ext=.py |>