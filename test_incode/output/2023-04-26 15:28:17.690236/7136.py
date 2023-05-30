#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or multiplyes all ports. """    
    while True:
        ports = input("Enter ports separated by comma: ")
        ports = ports.split(",")
        for port in ports:
            print(port, "is ", end='')
            if port == "quit":
                break
            else:
                print(" multiplied by ", end='')
                