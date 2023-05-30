#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and removes a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python3 remove-port.py <port>')
        sys.exit()
    
    port = sys.argv[1]
    
    ports = [int(i) for i in port.split(',')]
    
    ports.remove(port)
    
    print(','.join(str(i) for i in ports))
    
