#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))

<|/ file source=github ext=.py filename=word