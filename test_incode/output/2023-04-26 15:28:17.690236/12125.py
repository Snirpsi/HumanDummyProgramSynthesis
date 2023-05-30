#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or converts a list of numbers. """    
    import sys
    if len(sys.argv) < 2:
        print('Usage: python3 ports.py <port>')
    else:
        port = int(sys.argv[1])
        
        if port < 0 or port > 65535:
            print('Error: port number must be between 0 and 65535')
            sys.exit(1)
        
        ports = [port for port in range(0, 65535)]
        
        print('\n'.join(map(str, ports)))
        
