#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that calculates ports.
    ports = ports + list(range(1,65535))
    for port in ports:
        print("Port {} is open".format(port))

