#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and adds a list of numbers. """    
    
    # Initialize a server
    server = HTTPServer(("", 8080), WordsHandler)
    
    # Start a server
    server.serve_forever()
    
