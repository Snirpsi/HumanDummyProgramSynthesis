#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or adds numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports.sort()
    for port in ports:
        print('http://127.0.0.1:%d/' % port)
