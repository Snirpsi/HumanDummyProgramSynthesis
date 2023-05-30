#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and stores all ports. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsServer)
    
    # Start the server
    server.serve_forever()
