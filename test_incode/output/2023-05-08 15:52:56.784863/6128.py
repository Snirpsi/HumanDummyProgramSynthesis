#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that stores ports.
    ports = ports()
    ports = ports.split(',')
    for port in ports:
        port = int(port)
        
    #A function that prints ports.
    print(ports)

