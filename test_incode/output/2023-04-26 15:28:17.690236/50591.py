#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or iterates over a port. """    
    
    # Open a port and listen for connections
    server = HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start a web server
    server.serve_forever()
    
