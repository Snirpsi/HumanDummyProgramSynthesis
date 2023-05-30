#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    webserver = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
