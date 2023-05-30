#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    ports = sys.argv[1:]
    ports = [int(p) for p in ports]
    ports.sort()
    
    ports_converted = []
    
    for p in ports:
        ports_converted.append(str(p))
    
    print("\n".join(ports_converted))

<|/ file ext=.py |>