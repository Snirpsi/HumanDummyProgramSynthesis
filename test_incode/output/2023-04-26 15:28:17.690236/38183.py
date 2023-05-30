#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and returns a port. """    
    port = 1
    
    # Start a server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Wait forever
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
    # 