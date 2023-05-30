#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = int(sys.argv[1])
    
    # Create the webserver
    server = HTTPServer(('localhost', port), MyHandler)
    
    # Start the server
    server.serve_forever()
    
