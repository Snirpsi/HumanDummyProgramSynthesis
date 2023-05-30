#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or multiplyes user input. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
