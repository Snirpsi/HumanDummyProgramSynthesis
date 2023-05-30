#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or adds fruits. """    
    while True:
        print("Ports:")
        for port in get_ports():
            print(port)
        print("Fruits:")
        for fruit in get_fruits():
            print(fruit)
        print("Press enter to exit.")
        