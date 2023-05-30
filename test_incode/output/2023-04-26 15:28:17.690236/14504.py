#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Create a server and a handler to receive HTTP requests
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start a thread to handle requests
    server.serve_forever()
    
