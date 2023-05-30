#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or removes a port. """    
    
    port = input("Enter the port to enumerate: ")
    
    server_address = ('', int(port))
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    
    print('Server stopped.')
    
