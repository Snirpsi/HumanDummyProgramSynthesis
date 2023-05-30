#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    # Start a web server
    server = HTTPServer(("", 8000), WordConverter)
    
    # Start a web server
    server.serve_forever()
