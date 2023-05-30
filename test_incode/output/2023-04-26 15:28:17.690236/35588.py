#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or stores all ports. """    
    
    ports = []
    
    # Add ports to list
    ports.append(8080)
    ports.append(8088)
    ports.append(8089)
    ports.append(8090)
    
    # Store all ports
    ports = list(set(ports))
    
    # Print ports
    print('Ports:', ports)
    
    # Start webserver
    httpd = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
