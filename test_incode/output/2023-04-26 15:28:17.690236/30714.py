#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start a web server
    