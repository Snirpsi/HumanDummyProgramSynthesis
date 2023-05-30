#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or stores all ports. """    
    while True:
        try:
            ports = input("Enter ports: ")
            ports = ports.split()
            ports = [int(port) for port in ports]
            ports = list(set(ports))
            ports.sort()
            ports = ports[::-1]
            for port in ports:
                print(port)
        except EOFError:
            break
