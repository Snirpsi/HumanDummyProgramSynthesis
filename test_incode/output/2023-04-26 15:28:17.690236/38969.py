#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), MyHandler)
    
    # Start it
    server.serve_forever()
