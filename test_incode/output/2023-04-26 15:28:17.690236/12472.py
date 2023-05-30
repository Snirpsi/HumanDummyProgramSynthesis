#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and converts user input. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start a web server
    