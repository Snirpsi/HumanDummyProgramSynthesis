#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that converts all ports.
    #It will also print a message to the screen.
    #The port number will be the argument to the function.
    #The message will be the return value of the function.
    def convert(port):
        print("Port number " + str(port) + " is converted.")
        return port
    #The main function.
    convert(ports[0])

