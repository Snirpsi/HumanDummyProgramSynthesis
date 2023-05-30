#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and iterates over a list of words. """    
    
    
    # Read in the list of words from the command line
    wordlist = sys.argv[1:]
    
    # Remove all words from the list
    wordlist = [word for word in wordlist if word not in 