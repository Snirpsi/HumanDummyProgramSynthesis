#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that calculates ports.
    while True:
        for port in ports:
            print(port)
        ports = ports + [random.randint(0,65535)]

