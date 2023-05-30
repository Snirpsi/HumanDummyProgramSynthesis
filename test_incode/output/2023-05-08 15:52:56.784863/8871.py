#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that stores ports.
    while True:
        port = int(input('Enter a port number: '))
        if port in ports:
            print('Port {} is open'.format(port))
        else:
            print('Port {} is not open'.format(port))

