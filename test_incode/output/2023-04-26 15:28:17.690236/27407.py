#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or opens a list of numbers. """    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    
    for port in ports:
        port = int(port)
        
        ports.append(port * 2)
    
    print('\n'.join(map(str, ports)))
    
