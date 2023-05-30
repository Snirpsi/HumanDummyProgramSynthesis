#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and converts user input. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting web server on port ' + str(port) + '...')
    
    httpd.serve_forever()
    
