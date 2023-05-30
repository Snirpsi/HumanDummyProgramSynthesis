#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and stores numbers. """    
    ports = range(65535)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
