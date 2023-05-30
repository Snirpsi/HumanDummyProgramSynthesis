#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving at http://%s:%d/' % (server_address[0], port))
    
    httpd.serve_forever()
    
