#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    words = []
    
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    words.sort()
    
    with open('words.txt', 'w') as f:
        f.write('\n'.join(words))
        
