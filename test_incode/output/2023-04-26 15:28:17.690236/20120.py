#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and enumerates a port. """    
    
    ports = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    ports_enumerated = enumerate(ports)
    
    for port, number in ports_enumerated:
        print("Port {} has number {}".format(port, number))
    
    print("\nDone.")
    
