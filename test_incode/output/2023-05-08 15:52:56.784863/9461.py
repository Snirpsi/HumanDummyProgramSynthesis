#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that calculates ports.
    ports = ports + [random.randint(0,65535) for i in range(3)]
    print(ports)

