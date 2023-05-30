#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or multiplyes a port. """    
    
    ports = [int(i) for i in input().split()]
    
    ports_new = []
    
    for port in ports:
        
        if port % 2 == 0:
            ports_new.append(port)
        else:
            ports_new.append(port * 2)
    
    print(" ".join(str(x) for x in ports_new))
    
