#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or adds words. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    
    words = []
    
    for p in ports:
        words.append(str(p))
        
    words.append('')
    
    for word in words:
        print('