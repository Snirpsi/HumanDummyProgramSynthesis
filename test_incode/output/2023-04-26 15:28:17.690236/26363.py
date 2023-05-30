#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and multiplyes numbers. """    
    
    port = int(sys.argv[1])
    
    ports = [port * i for i in range(1, 100)]
    
    print('\n'.join(map(str, ports)))
    
