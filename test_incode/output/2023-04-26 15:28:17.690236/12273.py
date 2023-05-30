#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or opens numbers. """    
    
    import os
    import sys
    
    port = 8080
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    webserver_address = 'http://localhost:' + str(port)
    
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
