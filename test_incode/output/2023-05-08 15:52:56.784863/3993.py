#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that converts all ports.
    #It will run forever
    while True:
        for port in ports:
            print(port)
            time.sleep(1)

