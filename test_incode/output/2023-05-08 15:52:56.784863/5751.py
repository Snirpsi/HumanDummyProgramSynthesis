#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that calculates a port.
    while True:
        port = port + 1
        print('Port {} is now open.'.format(port))
        time.sleep(1)

