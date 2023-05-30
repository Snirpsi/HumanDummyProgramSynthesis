#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        port_converted = convert_port(port)
        print("The port number you entered is", port_converted)
        time.sleep(1)

<|/ file filename=port