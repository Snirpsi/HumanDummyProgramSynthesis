#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and multiplyes fruits. """    
    
    ports = range(0,65535)
    fruits = range(0,65535)
    
    for port in ports:
        for fruit in fruits:
            
            print("Port {} Fruit {}".format(port,fruit))
    
