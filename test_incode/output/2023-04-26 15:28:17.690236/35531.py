#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    ports = Ports.objects.all()
    for port in ports:
        print(port.name)
        print(port.description)
        print(port.