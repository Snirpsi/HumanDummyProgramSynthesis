#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that adds all ports.
    while True:
        ports.extend((random.randint(0,65535) for i in range(0,65535)))
        
    #A loop that prints all the ports.
    for port in ports:
        print(port)

