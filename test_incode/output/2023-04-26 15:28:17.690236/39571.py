#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or removes all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        
        if port not in ports:
            
            print("Port {} is not in list".format(port))
            
        else:
            
            ports.remove(port)
            
    print("Ports removed: {}".format(ports))
    
    
