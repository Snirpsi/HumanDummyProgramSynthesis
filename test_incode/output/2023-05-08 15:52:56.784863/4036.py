#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        for port in ports:
            print("Port {} is open".format(port))
        time.sleep(1)

