#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and iterates over all ports. """    
    
    fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'peach', 'plum', 'raspberry', 'strawberry', 'watermelon']
    
    while True:
        ports = []
        
        for fruit in fruits:
            ports.append(fruit)
            
        for port in ports:
            print(port)
            
        time.sleep(1)
        
