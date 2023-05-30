#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that prints a port.
    while True:
        time.sleep(1)
        print('Port is %s' % port)
        port = port + 1

