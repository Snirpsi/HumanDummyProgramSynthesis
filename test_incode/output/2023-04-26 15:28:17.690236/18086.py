#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or prints all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print('http://127.0.0.1:{}'.format(port))
        
