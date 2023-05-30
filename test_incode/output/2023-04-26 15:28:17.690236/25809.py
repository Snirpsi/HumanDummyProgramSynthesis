#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and prints all ports. """    
    
    ports = []
    
    # Add all ports
    for port in range(0, 65535):
        ports.append(port)
        
    # Print all ports
    for port in ports:
        print('Port {} is open'.format(port))
    
    # Start server
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
