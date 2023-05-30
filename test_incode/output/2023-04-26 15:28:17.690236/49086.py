#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or calculates all ports. """    
    
    port = 0
    
    try:
        port = int(sys.argv[1])
    except:
        port = 0
        
    if port == 0:
        port = 1
        
    ports = list(range(1,port+1))
    
    for port in ports:
        print("http://127.0.0.1:%d/" % port)
        
