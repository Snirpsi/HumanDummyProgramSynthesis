#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or stores a list of numbers. """    
    
    # Setup webserver
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    # Setup port list
    ports = []
    
    # Start webserver
    httpd.serve_forever()
    
    # Close webserver
    httpd.server_close()
    
    # Print port list
    print('Ports:')
    for port in ports:
        print('  {}'.format(port))
    
