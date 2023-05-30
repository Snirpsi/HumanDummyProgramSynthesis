#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    # Start a webserver
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start the webserver
    server.serve_forever()
