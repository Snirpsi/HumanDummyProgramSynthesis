#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or stores words. """    
    
    port = int(sys.argv[1])
    
    # Store the port in the database
    storePort(port)
    
    # Store the words in the database
    storeWords(port)
    
    # Serve the webpage
    serveWebpage(port)
    
