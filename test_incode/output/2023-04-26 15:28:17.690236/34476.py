#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        
        port = str(port)
        
        if port == '':
            continue
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print('Port number must be between 0 and 65535.')
            continue
        
        ports.append(port * 2)
        
    print('\n'.join(map(str, ports)))
    
