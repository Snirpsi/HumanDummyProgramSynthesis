#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and iterates over all ports. """    
    
    port = 1
    
    while True:
        port = port + 1
        
        print('Starting port {}'.format(port))
        
        webserver.serve_forever()
        
