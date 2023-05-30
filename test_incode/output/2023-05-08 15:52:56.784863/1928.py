#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that stores all ports.
    while True:
        ports.append(int(input('Enter a port number: ')))
        #A while loop that prints out the ports.
        while ports:
            print(ports.pop())

