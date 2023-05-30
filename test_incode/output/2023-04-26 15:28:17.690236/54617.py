#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and opens numbers. """    
    
    webserver_address = ('localhost', 8080)
    
    httpd = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
