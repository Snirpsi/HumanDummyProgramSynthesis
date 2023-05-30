#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
