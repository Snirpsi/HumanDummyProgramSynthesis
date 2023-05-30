#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and prints a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python server.py <port>')
        sys.exit()
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving on port 