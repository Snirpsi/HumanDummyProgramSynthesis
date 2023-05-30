#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and iterates over user input. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start a web server
    