#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    words.sort()
    
    print('\n'.join(words))
    
