#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and prints numbers. """    
    
    # Create a webserver object
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start up the server
    server.serve_forever()
    
