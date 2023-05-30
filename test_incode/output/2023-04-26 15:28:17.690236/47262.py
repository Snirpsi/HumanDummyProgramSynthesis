#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or removes all ports. """    
    ports = enumeratePorts(sys.argv[1])
    for port in ports:
        print(port)
    
<|/ file filename=enumeratePorts.py |>