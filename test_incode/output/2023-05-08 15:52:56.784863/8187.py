#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that adds all ports.
    while True:
        ports.extend((port for port in ports if port < 65535))
        #print(ports)
        time.sleep(1)

