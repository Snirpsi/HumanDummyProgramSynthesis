#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = glob.glob('/sys/class/net/*/iface_port')
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((port, 0))
            sock.close()
        except:
            pass
