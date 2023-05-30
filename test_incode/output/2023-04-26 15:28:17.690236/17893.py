#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or iterates over numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    while True:
        ports.sort()
        for port in ports:
            print(port)
        time.sleep(1)
