#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that calculates all ports.
    while True:
        ports.clear()
        for port in range(0,65535):
            ports.add(port)
        ports.sort();
        print(ports)
        time.sleep(1)

