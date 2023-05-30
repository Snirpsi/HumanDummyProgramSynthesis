#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    port = int(sys.argv[1])
    
    # Create a server and bind it to the port number.
    httpd = HTTPServer(('', port), MyHandler)
    
    # Start up the server.
    httpd.serve_forever()
    
