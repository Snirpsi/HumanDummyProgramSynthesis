#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and multiplyes user input. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    
    httpd.serve_forever()
    
