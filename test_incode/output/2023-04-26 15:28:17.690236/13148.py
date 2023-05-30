#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and opens all ports. """    
    while True:
        fruits = Fruits()
        fruits.open_ports()
        fruits.calculate_fruits()
        fruits.close_ports()
        time.sleep(2)
