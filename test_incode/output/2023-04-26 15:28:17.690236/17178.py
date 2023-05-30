#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    # Initialize a server
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Run the server
    server.serve_forever()
    
