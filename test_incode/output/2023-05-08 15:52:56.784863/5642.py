#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that returns ports.
    while True:
        ports.extend((random.randint(1024,65535) for _ in range(10)))
        print(ports)
        time.sleep(1)

