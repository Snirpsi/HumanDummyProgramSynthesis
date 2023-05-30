#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or multiplyes words. """    
    
    ports = range(1024)
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for port in ports:
        
        print('Starting port ' + str(port) + ' ...')
        
        for word in words:
            
            print('  ' + word)
            
            print('  ' + word * 