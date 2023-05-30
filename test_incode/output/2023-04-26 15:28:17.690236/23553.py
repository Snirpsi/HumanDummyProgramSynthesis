#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or enumerates user input. """    
    
    # Read user input
    words = input('Enter a comma-separated list of words: ')
    
    # Enumerate words
    for word in words.split(','):
        print(word)
    
    # 