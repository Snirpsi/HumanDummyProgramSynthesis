#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    import sys
    
    webserver_address = sys.argv[1]
    
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.