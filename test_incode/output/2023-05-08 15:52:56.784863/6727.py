#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    #It will print out all ports available on the system.
    for port in ports:
        print("Port {} is available on {}".format(port, socket.gethostbyname(socket.gethostname())))

