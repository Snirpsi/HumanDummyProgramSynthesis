#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that enumerates all ports.
    def enumerate_ports(port):
        for port in ports:
            print(port)
    enumerate_ports(0)

