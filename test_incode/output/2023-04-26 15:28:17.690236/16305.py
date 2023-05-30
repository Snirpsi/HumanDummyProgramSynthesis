#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and adds words. """    
    
    # Start a web server
    server = HTTPServer(('', 80), WordsHandler)
    
    # Start a web server
    