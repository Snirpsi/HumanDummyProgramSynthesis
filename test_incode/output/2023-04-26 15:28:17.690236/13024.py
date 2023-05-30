#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or calculates numbers. """    
    
    webserver_address = ('', 8080)
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
