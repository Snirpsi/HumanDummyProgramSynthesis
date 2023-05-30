#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that removes ports.
    while True:
        ports.remove( int(input('Enter a port number: ')))
        if ports == []:
            break
    print('Ports removed')

