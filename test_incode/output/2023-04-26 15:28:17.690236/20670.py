#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or stores all ports. """    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        if ports[-1] == 'exit':
            break
        else:
            print("Multiplying ports {} 