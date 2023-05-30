#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input('Enter a filename: ')
    
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                words.append(line)
    
    print('\n'.join(words))
    
