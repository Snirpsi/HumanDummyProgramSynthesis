#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or iterates over a port. """    
    import sys
    port = int(sys.argv[1])
    
    if port == -1:
        port = 0
    
    ports = [port]
    
    while True:
        try:
            line = sys.stdin.readline()
            
            if line == '':
                break
            
            ports.append(int(line))
            
        except KeyboardInterrupt:
            break
        
    ports.sort()
    
    for port in ports:
        print('Port {}: {}'.format(port, 