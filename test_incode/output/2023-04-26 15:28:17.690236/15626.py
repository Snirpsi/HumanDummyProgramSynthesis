#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and removes a list of words. """    
    port = int(sys.argv[1]) 
    words = sys.argv[2:]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    for word in words:
        httpd.