#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that removes all ports.
    while True:
        ports.remove(ports.pop())
        
    #A loop that prints the ports one by one.
    for port in ports:
        print(port)

