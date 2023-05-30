#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and converts a port. """    
    
    port = int(sys.argv[1])
    
    fruits = ("apple", "orange", "banana", "cherry")
    
    fruits_sum = sum(fruits)
    
    fruits_converted = [fruit * 