#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that opens ports.
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        listen(port)

