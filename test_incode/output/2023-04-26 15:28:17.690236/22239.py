#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    words = [sys.argv[2]]
    
    words.extend(sys.argv[3:])
    
    port = int(port)
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
