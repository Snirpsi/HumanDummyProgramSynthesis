#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and enumerates a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for port in range(port, 65535):
        numbers.append(port)
    print("\n".join(str(n) for n in numbers))

<|/ file ext=.py filename=