#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that removes ports.
    ports.remove('8080')
    #A function that adds ports.
    ports.append('8080')
    #A function that prints ports.
    print(ports)

