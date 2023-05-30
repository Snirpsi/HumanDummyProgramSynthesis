#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python webserver.py <port>')
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting web server on port %s' % port)
    httpd.serve_forever()
    
