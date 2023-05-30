#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or returns a port. """    
    port = int(input("Enter a port number: "))
    
    # Create a server
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
    # Close the socket
    socket.close()
    
    # Close the terminal
    