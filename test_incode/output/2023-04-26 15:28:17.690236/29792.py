#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or opens numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
