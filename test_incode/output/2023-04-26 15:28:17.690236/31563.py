#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and multiplyes words. """    
    
    # Create a server
    server = HTTPServer(("", 8080), MyHandler)
    
    # Start the server
    server.serve_forever()
