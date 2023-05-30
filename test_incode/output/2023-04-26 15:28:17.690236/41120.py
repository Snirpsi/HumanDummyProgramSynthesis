#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports and calculates fruits. """    
    
    ports = Ports()
    fruits = Fruits(ports)
    
    while True:
        fruits.update()
        
        if fruits.has_fruit():
            print(