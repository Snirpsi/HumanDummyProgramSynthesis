#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that adds ports.
    while True:
        ports.append(random.randint(0,65535))
        time.sleep(1)

