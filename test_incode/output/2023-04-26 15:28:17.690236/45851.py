#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Create a server and listen on port 80
    server = HTTPServer(('', 80), MyHandler)
    
    # Start the server
    server.serve_forever()
    
