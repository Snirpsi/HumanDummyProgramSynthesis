#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or stores all ports. """    
    
    while True:
        ports = input('Enter ports: ')
        ports = ports.split()
        ports = [int(p) for p in ports]
        
        if ports == []:
            break
        
        ports.sort()
        
        for p in ports:
            print(p)
            
        print('')
        
