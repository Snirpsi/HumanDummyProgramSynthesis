#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port> <words>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    words = [w.strip() for w in words]
    
    ports = [port * int(w) for w in words]
    
    print('\n'.join(map(str, ports)))
    
