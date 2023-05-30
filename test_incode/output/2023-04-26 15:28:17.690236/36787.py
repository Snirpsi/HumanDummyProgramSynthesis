#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and stores a list of numbers. """    
    
    # Get the list of words from the command line
    words = sys.argv[1:]
    
    # Remove all words from the list
    words = [w for w in words if w not in ['-','--','--help','-h','--version']]
    
    # Print the list of words to the screen
    print('\n'.join(words))
    
    # Print the list of numbers to the screen
    print('\n'.join(map(str, range(1,10))))
    
    # Run the server
    webserver()
    
