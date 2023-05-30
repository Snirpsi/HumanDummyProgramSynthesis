#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and removes a port. """    
    import sys
    
    # Read command line arguments
    words = sys.argv[1:]
    
    # Convert words to ports
    ports = map(int, words)
    
    # Remove ports
    ports = list(filter(lambda x: x is not None, ports))
    
    # Print ports
    for port in ports:
        print('Port {}'.format(port))
    
    # 