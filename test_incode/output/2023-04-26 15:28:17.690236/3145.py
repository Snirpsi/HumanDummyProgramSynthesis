#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving at http://%s:%d/' % (server_address[0], server_address[1]))
    
    httpd.serve_forever()
    
