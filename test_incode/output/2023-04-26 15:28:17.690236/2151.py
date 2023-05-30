#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    # Open the wordlist
    wordlist = open('wordlist.txt', 'r')
    
    # Read the wordlist into a list
    wordlist = wordlist.read().splitlines()
    
    # Print the wordlist
    for word in wordlist:
        print(word)
    
    # Close the wordlist
    wordlist.close()
    
    # Start the webserver
    webserver.serve_forever()
    
