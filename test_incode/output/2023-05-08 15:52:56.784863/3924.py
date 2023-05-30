#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that enumerates all ports.
    #This function is called from main() when this script is run.
    ports = enumerate_ports()
    #A function that prints the ports.
    #This function is called from main() when this script is run.
    print_ports(ports)

