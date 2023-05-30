#!/usr/bin/python3
if __name__ == '__main__':
    #A program that removes all ports.
    ports = input("Enter the ports to remove: ")
    ports = ports.split()
    for port in ports:
        remove_port(port)
    print("Done")

