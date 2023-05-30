#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and removes words. """    
    
    # Start server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start server
    server.serve_forever()
    
