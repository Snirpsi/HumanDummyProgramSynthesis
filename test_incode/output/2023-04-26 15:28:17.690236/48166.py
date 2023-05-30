#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or iterates over user input. """    
    while True:
        ports = input("Enter ports (comma separated): ")
        ports = ports.split(",")
        for port in ports:
            port = int(port)
            if port < 0 or port > 65535:
                print("Port number must be between 0 and 65535")
            else:
                