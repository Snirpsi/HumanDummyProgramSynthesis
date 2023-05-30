#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    
    ports = open('/proc/net/tcp','r').read().splitlines()
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((port