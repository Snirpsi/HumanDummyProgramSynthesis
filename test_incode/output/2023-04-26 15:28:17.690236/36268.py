#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    
    words = []
    
    # Read words from a file
    with open('words.txt', 'r') as f:
        words = [line.strip() for line in f]
    
    # Write words to a file
    with open('words.txt', 'w') as f:
        f.write('\n'.join(words))
    
    print('Done.')
    
