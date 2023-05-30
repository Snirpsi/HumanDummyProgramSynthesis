#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that stores ports.
    while True:
        ports.append(int(input('Enter a port number: ')))
        #A while loop that prints ports.
        while ports:
            print(ports.pop())

