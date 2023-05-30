#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that converts ports.
    while True:
        port = str(input('Enter a port number: '))
        if port in ports:
            print(port)
        else:
            print('Invalid port number')

