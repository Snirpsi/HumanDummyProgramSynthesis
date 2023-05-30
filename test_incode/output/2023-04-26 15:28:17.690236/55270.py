#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Start server
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()
