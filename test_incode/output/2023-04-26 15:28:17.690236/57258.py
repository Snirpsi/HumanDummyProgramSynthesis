#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or stores all ports. """    
    while True:
        ports = input('Enter a port number or enter a key to stop: ')
        if ports == '':
            break
        ports = ports.strip()
        if ports == 'key':
            break
        ports = ports.split(',')
        ports = [int(p) for p in ports]
        ports = [p for p in ports if p >= 0 and p < 65535]
        ports.sort()
        for p in ports:
            print(p)
            
<|/ file filename=ports.py source=github |>