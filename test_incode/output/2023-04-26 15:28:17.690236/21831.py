#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or prints user input. """    
    
    # Start a web server
    server = HTTPServer(("", 80), MyHandler)
    
    # Start a web server
    