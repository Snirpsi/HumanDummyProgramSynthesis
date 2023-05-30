#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or prints a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    print('\n'.join(map(str, ports)))
