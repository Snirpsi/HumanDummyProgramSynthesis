#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), MyHandler)
    
    # Run the server
    server.serve_forever()
    
