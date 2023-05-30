#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that calculates all ports.
    while True:
        ports = list(ports)
        ports.reverse()
        for port in ports:
            print(port)
            time.sleep(1)

