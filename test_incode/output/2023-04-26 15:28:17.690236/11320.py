#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or opens user input. """    
    ports = input("Enter ports (comma separated): ")
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    ports.sort()
    for port in ports:
        print("Port {} is open".format(port))
    
