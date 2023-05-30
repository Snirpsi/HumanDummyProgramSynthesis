#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = calculate_fruits(100)
        print("Fruits are", fruits)
        time.sleep(1)
