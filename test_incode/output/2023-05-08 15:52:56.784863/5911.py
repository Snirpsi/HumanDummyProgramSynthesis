#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that returns ports.
    while True:
        ports.clear()
        for port in ports:
            ports.append(port)
        ports.sort()
        print(ports)
        time.sleep(1)

