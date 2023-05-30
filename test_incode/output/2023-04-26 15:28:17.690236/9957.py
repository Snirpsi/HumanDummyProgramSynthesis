#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and returns all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        print("http://127.0.0.1:%d/" % port)
    
