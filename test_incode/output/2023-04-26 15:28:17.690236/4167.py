#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    # Create a webserver instance
    server = HTTPServer(("", PORT), MyHandler)
    
    # Start it
    server.serve_forever()
    
