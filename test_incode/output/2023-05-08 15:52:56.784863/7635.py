#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that removes all ports.
    while True:
        ports.remove(0)
        
    #A loop that prints out the ports currently in use.
    for port in ports:
        print(port)

