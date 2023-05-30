#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or stores user input. """    
    
    # Create the server
    server = HTTPServer(('localhost', 8080), MyHandler)
    
    # Start the server
    server.serve_forever()
    
