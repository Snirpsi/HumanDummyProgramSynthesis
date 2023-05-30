#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or iterates over a list of words. """    
    
    # Read list of words from stdin and store in list
    words = [word.strip() for word in sys.stdin.read().split()]
    
    # Iterate over words and print each word with its 