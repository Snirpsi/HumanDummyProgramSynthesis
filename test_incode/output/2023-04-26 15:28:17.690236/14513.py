#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and enumerates numbers. """    
    
    # Create a server
    server = HTTPServer(("", 8000), MyHandler)
    
    # Start it
    server.serve_forever()
    
