#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and removes a port. """    
    
    port = 5000
    
    # Create a server and a client to communicate with each other
    server = BaseHTTPServer.HTTPServer(('', port), MyHandler)
    
    # Start the server
    server.serve_forever()
    
