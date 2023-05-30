#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or stores a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in ports:
            print(ports[word])
        else:
            ports[word] = len(ports)
            print(ports[word])
    else:
        print('Usage: python ports.py word')
        
