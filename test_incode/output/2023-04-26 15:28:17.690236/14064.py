#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    # Loop forever
    while True:
        # Print the word and its index
        print('{}: {}'.format(words[