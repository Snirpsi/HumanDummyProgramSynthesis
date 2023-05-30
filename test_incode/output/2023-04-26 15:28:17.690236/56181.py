#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    
    # Read words from file
    words = []
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Add words to list
    words.extend(['the', 'cat', 'is', 'a', 'dog'])
    
    # Print list
    print('\n'.join(words))
    
    # Write list to file
    with open('words.txt', 'w') as f:
        f.write('\n'.join(words))
    
    # 