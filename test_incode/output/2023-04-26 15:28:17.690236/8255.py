#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and converts numbers. """    
    while True:
        ports = os.listdir('/sys/class/net/')
        for port in ports:
            if  port.isdigit():
                os.remove('/sys/class/net/' + port)
            else:
                os.remove('/sys/class/net/' + port + '/