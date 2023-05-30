#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or adds a list of words. """    
    
    # Get the command line arguments
    arguments = docopt(__doc__)
    
    # Get the list of words from the command line
    wordlist = arguments['words']
    
    # Iterate over the wordlist and add each word to the webserver
    for word in wordlist:
        
        # Add the word to the webserver
        