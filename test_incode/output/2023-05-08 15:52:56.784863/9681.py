#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that stores all ports.
    while True:
        ports.append(getPort())
        time.sleep(1)

