#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that calculates all ports.
    while True:
        ports.extend((random.randint(0,65535) for i in range(0,65535)))
        print(ports)
        time.sleep(1)

