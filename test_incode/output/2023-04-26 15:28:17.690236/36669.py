#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for port in range(1, 65535):
        words.append(str(port))
    
    print("\n".join(words))
    
