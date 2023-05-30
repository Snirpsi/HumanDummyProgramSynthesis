#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports. """    
    while True:
        ports = socket.getservbyname('http', 'tcp')
        for port in ports:
            print(port)
        time.sleep(1)
