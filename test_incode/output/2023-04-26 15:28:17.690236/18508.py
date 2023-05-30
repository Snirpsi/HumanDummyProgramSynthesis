#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and iterates over user input. """    
    port = int(input('Enter a port number: '))
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    httpd.serve_forever()
    
