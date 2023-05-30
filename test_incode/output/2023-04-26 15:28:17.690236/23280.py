#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or prints user input. """    
    while True:
        ports = input("Enter ports separated by spaces (no spaces allowed): ")
        if ports == "":
            break
        ports = ports.split()
        for port in ports:
            port = int(port)
            if port > 65535:
                print("Port number must be less than 65535")
            else:
                