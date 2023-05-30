#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = fruits_calculator()
        print("Fruits: ", fruits)
        time.sleep(1)
