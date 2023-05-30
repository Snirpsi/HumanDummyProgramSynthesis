#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that returns ports.
    while True:
        ports.reverse()
        for port in ports:
            print(port)
        time.sleep(1)

