#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and calculates a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
