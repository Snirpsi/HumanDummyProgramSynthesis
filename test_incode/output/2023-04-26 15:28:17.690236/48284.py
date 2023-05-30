#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    print(" ".join(words))
    
