#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    # Start the server
    server = HTTPServer(('localhost', 8080), WordsHandler)
    
    # Run the server
    server.serve_forever()
