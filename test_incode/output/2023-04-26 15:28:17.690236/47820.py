#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = int(sys.argv[1])
    
    # Create the server
    server = HTTPServer(("", port), MyHandler)
    
    # Start the server
    server.serve_forever()
    
