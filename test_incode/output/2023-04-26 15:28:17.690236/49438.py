#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or removes a list of numbers. """    
    
    # Create the web server
    server = HTTPServer(("", 8080), WordsServer)
    
    # Start the server
    server.serve_forever()
    
