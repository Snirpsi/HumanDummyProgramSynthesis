#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that converts all ports.
    #It will take as input the ports range and will convert them into hexadecimal values.
    #The output will be a list with the hexadecimal values.
    ports_hex = ports_to_hex( ports )
    print(ports_hex)

