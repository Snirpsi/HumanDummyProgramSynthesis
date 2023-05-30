#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and iterates over all ports. """    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
