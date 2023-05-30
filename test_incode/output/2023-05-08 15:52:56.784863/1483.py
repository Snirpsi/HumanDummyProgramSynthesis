#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that opens ports.
    for port in ports:
        openport(port)
else:
    #A program that closes ports.
    for port in ports:
        closeport(port)

