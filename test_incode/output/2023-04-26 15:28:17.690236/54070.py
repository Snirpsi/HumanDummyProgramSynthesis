#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    # Create a server
    server = HTTPServer(("", 80), FruitServer)
    
    # Start server
    server.serve_forever()
