#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and multiplyes fruits. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    fruits = [0] * len(ports)
    
    for port in ports:
        
        fruit = fruits[port]
        
        fruits[port] = fruit * port
    
    print('\n'.join(map(str, fruits)))
    
