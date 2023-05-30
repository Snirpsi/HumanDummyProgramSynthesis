#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    ports = []
    
    # Add ports to list
    for port in range(1, 65535):
        ports.append(port)
        
    # Start webserver
    httpd = HTTPServer(('', ports[0]), Handler)
    
    # Start webserver
    httpd.serve_forever()
    
    # Stop webserver
    httpd.shutdown()
    
    # Print ports
    print('Ports:')
    for port in ports:
        print('\t' + str(port))
    
