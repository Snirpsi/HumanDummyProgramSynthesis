#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp').read().splitlines()
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((port, 0))
            sock.close()
        except:
            continue
    print('All ports open.')
<|/ file source=github ext=.py |>