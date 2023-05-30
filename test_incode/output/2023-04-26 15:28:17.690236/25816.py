#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and stores user input. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
