#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or removes user input. """    
    
    # Start a webserver
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
