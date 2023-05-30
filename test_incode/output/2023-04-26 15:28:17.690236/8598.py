#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and converts all ports. """    
    while True:
        ports = openports()
        for port in ports:
            ports[port] = convertport(port)
        ports = ports.items()
        ports.sort()
        for port, value in ports:
            print(port, value)
        time.sleep(1)

<|/ file ext=.py filename=ports.py |>