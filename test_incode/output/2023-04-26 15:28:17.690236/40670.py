#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    webserver_address = sys.argv[1]
    
    webserver_address = int(webserver_address)
    
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    
    webserver.serve_forever()
    
