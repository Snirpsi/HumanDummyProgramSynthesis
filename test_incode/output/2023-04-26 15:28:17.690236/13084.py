#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or stores a list of words. """    
    
    # Get the words from the command line and store them in a list
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    # Add the words to the server
    server = Server()
    server.add(words)
    
    # Start the server
    server.start()
    
    # Run the server
    server.serve_forever()
    
