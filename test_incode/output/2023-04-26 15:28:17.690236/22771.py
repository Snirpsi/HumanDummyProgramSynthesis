#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    fruits = Fruits()
    while True:
        fruits.calculate()
        time.sleep(.1)
    
