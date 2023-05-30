#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or adds words. """    
    while True:
        ports = os.listdir('/sys/class/net/')
        for port in ports:
            if port.startswith('eth'):
                os.remove('/sys/class/net/'+port)
            else:
                os.rename('/sys/class/net/'+port, '/sys/class/net/'+port+'