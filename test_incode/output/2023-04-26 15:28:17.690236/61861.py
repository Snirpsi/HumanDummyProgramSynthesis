#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or iterates over user input. """    
    while True:
        ports = input("Enter ports: ")
        if ports == '':
            break
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            if port > 65535:
                print("Port number {} is out of range".format(port))
            else:
                print("Port number {} is valid".format(port))
