#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or removes a list of numbers. """    
    while True:
        port = input("Enter a port number: ")
        if port == "":
            print("Port number cannot be empty!")
            continue
        port = int(port)
        if port not in range(1,65535):
            print("Port number must be between 1 and 65535!")
            continue
        if port in ports:
            ports.remove(port)
        else:
            ports.append(port)
        print("Port number {} has been added!".format(port))
        print("Press enter to exit.")
        input()
    
