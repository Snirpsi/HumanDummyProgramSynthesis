#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and adds a port. """    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_sum = sum(fruits)
    
    fruits_port = []
    
    for fruit in fruits:
        fruits_port.append(fruit)
        
    fruits_port.append(fruits_sum)
    
    fruits_port.append(port)
    
    fruits_port.reverse()
    
    print('\n'.join(