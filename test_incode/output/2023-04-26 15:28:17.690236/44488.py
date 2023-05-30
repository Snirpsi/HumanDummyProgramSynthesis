#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and stores all ports. """    
    
    # Create a simple webserver
    server = HTTPServer(("", 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
    # Stop it
    server.socket.close()
    
    # 