#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and prints a list of numbers. """    
    
    # Read the list of words from the command line
    wordlist = sys.argv[1]
    
    # Remove all words from the list
    wordlist = wordlist.split()
    
    # Print the list of numbers
    for word in wordlist:
        print(word)
        
    # Run the webserver
    webserver.serve_forever()
    
