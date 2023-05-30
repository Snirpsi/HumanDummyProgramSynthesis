#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and iterates over fruits. """    
    
    ports = []
    
    # Iterate over all available ports
    for port in range(0, 65535):
        ports.append(port)
        
    # Print all ports
    print('Available ports:')
    for port in ports:
        print('    {}'.format(port))
    
    # Start the server
    httpd = HTTPServer(('', port), MyHandler)
    
    # Start the server
    httpd.serve_forever()
    
