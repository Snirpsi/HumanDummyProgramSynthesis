#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that calculates ports.
    ports = [666,8080,80,443,22,3]
    ports = [int(port) for port in ports]
    print(ports)

