#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or multiplyes numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = [p * 2 for p in ports]
    print('\n'.join(map(str, ports)))

<|/ file source=github filename=