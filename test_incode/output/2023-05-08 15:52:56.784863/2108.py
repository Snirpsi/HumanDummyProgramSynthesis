#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    #Usage: python port2ip.py <port>
    import sys
    port = sys.argv[1]
    ipaddr = socket.gethostbyname(socket.gethostname())
    ipaddr = ipaddr + ':' + str(port)
    print(ipaddr)

