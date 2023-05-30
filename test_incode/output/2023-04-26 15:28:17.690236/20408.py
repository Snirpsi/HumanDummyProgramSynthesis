#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or prints user input. """    
    
    # Get the list of words from the command line
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    # Print the list of words to the user
    print('\n'.join(words))
    
    # Run the webserver
    webserver(words)
    
