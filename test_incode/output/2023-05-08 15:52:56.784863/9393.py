#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that converts all ports.
    #It takes one argument, port, which is a port number.
    #It returns all ports starting with that number.
    #It also prints out the port number.
    def ports_generator(port):
        for port in ports:
            if port == port:
                print(port)
            else:
                ports_generator(port)
    ports_generator(ports[0])

