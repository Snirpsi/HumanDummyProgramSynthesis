#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or multiplyes a port. """    
    
    # Create a server
    server = HTTPServer(("", 8000), WordsServer)
    
    # Start server
    server.serve_forever()
    
