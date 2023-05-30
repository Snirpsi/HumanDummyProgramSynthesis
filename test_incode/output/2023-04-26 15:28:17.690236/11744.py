#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or adds a port. """    
    
    # Create a web server
    server = HTTPServer(("", 80), MyHandler)
    
    # Start a web server
    server.serve_forever()
    
