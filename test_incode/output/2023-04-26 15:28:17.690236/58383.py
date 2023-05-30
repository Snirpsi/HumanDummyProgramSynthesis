#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    # Create the server
    server = HTTPServer(('', 80), MyHandler)
    
    # Run the server
    server.serve_forever()
