#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or prints fruits. """    
    port = int(input("Enter a port number: "))
    fruits = convert_port(port)
    print("The fruits of port {} are:".format(port))
    for fruit in fruits:
        print(fruit)
