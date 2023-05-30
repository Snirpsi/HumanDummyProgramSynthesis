#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or multiplyes fruits. """    
    
    ports = [
        (1, "Apple"),
        (2, "Banana"),
        (3, "Orange"),
        (4, "Mango"),
        (5, "Grape")
    ]
    
    fruits = ["Apple", "Banana", "Orange", "Mango", "Grape"]
    
    for port, fruit in zip(ports, fruits):
        print("{0} x {1} = {2}".format(port, fruit, port * fruit))
    
    print("Done!")
    
