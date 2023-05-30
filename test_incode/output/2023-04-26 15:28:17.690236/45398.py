#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports and enumerates fruits. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        print("\nPort: ", port)
        
        fruit = enumerate_fruit(port)
        
        for fruit in fruit:
            
            print("\t", fruit)
            
    print("\nDone.")
    
    
