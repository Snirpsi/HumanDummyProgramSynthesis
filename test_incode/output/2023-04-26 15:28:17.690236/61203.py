#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or converts a list of numbers. """    
    ports = range(1024)
    while True:
        ports_str = ','.join(map(str, ports))
        print(ports_str)
        ports = ports + 1
        time.sleep(1)
