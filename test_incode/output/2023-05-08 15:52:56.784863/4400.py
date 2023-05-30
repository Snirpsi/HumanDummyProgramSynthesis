#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that calculates ports.
    ports = calculate_ports(ports)
    #A function that prints the ports.
    print_ports(ports)

