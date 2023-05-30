#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 ports_multiply.py <ports>')
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        ports_multiply(port)
        
    print('Done.')
    
