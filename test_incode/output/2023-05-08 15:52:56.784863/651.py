#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that converts ports.
    #Usage: python ports.py [port]
    #Example: python ports.py 8080
    port = int(sys.argv[1])
    ports[port] = str(port)
    print(ports)

