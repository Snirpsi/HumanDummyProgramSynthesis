#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that stores ports.
    ports = ports + [8888]
    
    #A program that prints the ports.
    for port in ports:
        print(port)

