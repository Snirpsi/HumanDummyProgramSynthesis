#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and prints numbers. """    
    port = int(sys.argv[1])
    
    # Create a server to listen on port 8080
    server = HTTPServer(('', port), MyHandler)
    
    # Start the server
    server.serve_forever()
