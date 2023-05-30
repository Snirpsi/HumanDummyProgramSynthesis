#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and adds words. """    
    port = int(sys.argv[1])
    wordlist = sys.argv[2]
    
    remove_port(port, wordlist)
    
