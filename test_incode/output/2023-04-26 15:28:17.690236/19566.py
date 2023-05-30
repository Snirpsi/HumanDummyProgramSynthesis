#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    import sys
    ports = []
    for port in sys.argv[1:]:
        try:
            ports.append(int(port))
        except ValueError:
            print('Invalid port number')
            sys.exit(1)
    
    print('\n'.join(map(str, ports)))

<|/ file ext=.py source=github |>