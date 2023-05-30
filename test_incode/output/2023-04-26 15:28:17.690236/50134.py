#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or prints fruits. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()
    
