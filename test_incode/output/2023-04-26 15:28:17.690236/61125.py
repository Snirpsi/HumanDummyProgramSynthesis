#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and enumerates all ports. """    
    fruits = ['apple', 'banana', 'cherry']
    ports = []
    
    while True:
        fruits.append(input('Enter a fruit: '))
        ports.append(input('Enter a port: '))
        
        if len(ports) == 3:
            break
        
    print('\n'.join([f'{fruit} {port}' for fruit, port in zip(fruits, ports)]))
    
