#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and enumerates words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting web server at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()
