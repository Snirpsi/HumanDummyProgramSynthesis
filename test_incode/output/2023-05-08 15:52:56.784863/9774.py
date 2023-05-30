#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that prints a port.
    while True:
        port = port + 1
        print('Port {} is open'.format(port))
        time.sleep(1)

