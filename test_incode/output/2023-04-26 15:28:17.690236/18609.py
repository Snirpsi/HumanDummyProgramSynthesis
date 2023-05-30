#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_close = []
    
    # Loop over all ports we know about
    for port in range(1, 65535):
        
        # Close the port if we're not using it
        if port not in ports_to_close:
            
            # Open the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            # Close the port when it's no longer needed
            sock.close()
            
            # Add it to the list of ports to close
            ports_to_close.append(port)
            
    # Close the ports we closed
    for port in ports_to_close:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        sock.close()
        
    # Run the server
    httpd = HTTPServer(("", 0), MyHandler)
    httpd.serve_forever()
    
