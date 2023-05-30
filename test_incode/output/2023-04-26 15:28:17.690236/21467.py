#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and stores all ports. """    
    ports = []
    while True:
        ports.append(get_port())
        print('Port number: ' + str(ports[-1]))
        time.sleep(1)
    
